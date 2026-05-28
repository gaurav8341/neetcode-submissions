"""
Runs on every push to main via GitHub Actions.

1. AUTO-DISCOVER new problem folders not in problems.json
   → calls LeetCode GraphQL API to get topic tags
   → maps tags to our topic buckets (100% accurate)
   → falls back to keyword matching if API fails
2. SYNC solved status for all problems in the bank
"""
import json
import os
import re
import time
from pathlib import Path

try:
    import requests
except ImportError:
    import subprocess
    subprocess.run(["pip", "install", "requests", "-q"])
    import requests

# ── LC tag → our topic mapping ────────────────────────────────────────────────
LC_TAG_TO_TOPIC = {
    "depth-first-search":    ("hard", "graphs-bfs-dfs"),
    "breadth-first-search":  ("hard", "graphs-bfs-dfs"),
    "matrix":                ("hard", "graphs-bfs-dfs"),
    "topological-sort":      ("hard", "graphs-topo-sort"),
    "union-find":            ("hard", "graphs-advanced"),
    "shortest-path":         ("hard", "graphs-advanced"),
    "graph":                 ("hard", "graphs-bfs-dfs"),
    "tree":                  ("hard", "trees"),
    "binary-tree":           ("hard", "trees"),
    "binary-search-tree":    ("hard", "trees"),
    "heap-priority-queue":   ("hard", "heaps"),
    "sliding-window":        ("hard", "sliding-window"),
    "binary-search":         ("hard", "binary-search"),
    "backtracking":          ("hard", "backtracking"),
    "dynamic-programming":   ("hard", "dp-1d"),
    "trie":                  ("hard", "tries"),
    "monotonic-stack":       ("hard", "monotonic-stack"),
    "divide-and-conquer":    ("hard", "binary-search"),
    "recursion":             ("hard", "backtracking"),
    "stack":                 ("easy", "stack-queue"),
    "queue":                 ("easy", "stack-queue"),
    "monotonic-queue":       ("easy", "stack-queue"),
    "array":                 ("easy", "arrays"),
    "two-pointers":          ("easy", "arrays"),
    "prefix-sum":            ("easy", "arrays"),
    "hash-table":            ("easy", "hashmaps"),
    "string":                ("easy", "strings"),
    "string-matching":       ("easy", "strings"),
    "linked-list":           ("easy", "linked-list"),
    "sorting":               ("easy", "sorting"),
    "counting-sort":         ("easy", "sorting"),
    "greedy":                ("easy", "greedy"),
    "bit-manipulation":      ("easy", "math-bit"),
    "math":                  ("easy", "math-bit"),
    "number-theory":         ("easy", "math-bit"),
}

# Hard topics take priority over easy ones
HARD_TOPICS = {"graphs-bfs-dfs", "graphs-topo-sort", "graphs-advanced", "trees",
               "heaps", "sliding-window", "binary-search", "backtracking",
               "dp-1d", "dp-2d", "tries", "monotonic-stack"}

# ── Keyword fallback (used if API fails) ──────────────────────────────────────
TOPIC_RULES = [
    ("graphs-bfs-dfs",   ["island", "flood-fill", "clone-graph", "surrounded", "pacific",
                          "rotting", "word-ladder", "bipartite", "01-matrix", "treasure"]),
    ("graphs-topo-sort", ["course-schedule", "alien-dictionary", "parallel-courses", "minimum-height-trees"]),
    ("graphs-advanced",  ["network-delay", "cheapest-flights", "redundant-connection",
                          "connected-components", "swim-in-rising", "valid-tree"]),
    ("trees",            ["binary-tree", "inorder", "preorder", "postorder", "level-order",
                          "serialize", "lowest-common-ancestor", "balanced-binary",
                          "invert-binary", "subtree", "diameter", "path-sum", "right-side-view",
                          "good-nodes", "kth-smallest-element-in-a-bst", "validate-binary"]),
    ("heaps",            ["median", "data-stream", "merge-k-sorted", "kth-largest",
                          "k-closest", "task-scheduler", "reorganize-string", "design-twitter",
                          "stone-weight", "pass-ratio"]),
    ("sliding-window",   ["longest-substring-without", "sliding-window-maximum", "minimum-window",
                          "permutation-in-string", "repeating-character-replacement",
                          "erasure-value", "subarray-of-1s", "maximum-fruits-harvested"]),
    ("binary-search",    ["rotated-sorted-array", "minimum-in-rotated", "median-of-two",
                          "search-a-2d-matrix", "eating-bananas", "capacity-to-ship",
                          "peak-element", "time-based-key-value"]),
    ("backtracking",     ["combination-sum", "palindrome-partitioning", "letter-combinations",
                          "sudoku", "n-queens", "word-search", "permutations", "subsets"]),
    ("dp-1d",            ["climbing-stairs", "house-robber", "longest-increasing-subsequence",
                          "coin-change", "word-break", "target-sum", "longest-valid-parentheses"]),
    ("dp-2d",            ["longest-common-subsequence", "edit-distance", "coin-change-ii",
                          "count-square-submatrices", "burst-balloons", "pascals-triangle"]),
    ("tries",            ["implement-trie", "prefix-tree", "add-and-search-words",
                          "word-search-ii", "suffix-queries", "common-suffix", "trie"]),
    ("monotonic-stack",  ["largest-rectangle", "next-greater", "daily-temperatures", "subarray-minimums"]),
    ("arrays",           ["two-sum", "buy-and-sell", "product-of-array", "maximum-subarray",
                          "container-with-most-water", "trapping-rain", "merge-intervals",
                          "remove-one-element-to-make", "strictly-increasing"]),
    ("hashmaps",         ["group-anagrams", "anagram-groups", "longest-consecutive",
                          "subarray-sum-equals", "top-k-frequent", "lru-cache"]),
    ("strings",          ["valid-palindrome", "valid-anagram", "encode-and-decode",
                          "longest-palindromic", "valid-parentheses", "add-strings"]),
    ("stack-queue",      ["min-stack", "minimum-stack", "evaluate-reverse-polish",
                          "generate-parentheses", "car-fleet", "validate-parentheses"]),
    ("linked-list",      ["reverse-linked-list", "merge-two-sorted-list", "linked-list-cycle",
                          "remove-nth-node", "reorder-list", "add-two-numbers",
                          "reverse-nodes-in-k", "copy-list-with-random"]),
    ("sorting",          ["sort-colors", "sort-list", "largest-number", "sort-matrix"]),
    ("greedy",           ["assign-cookies", "non-overlapping-intervals", "partition-labels",
                          "matching-players", "maximum-events"]),
    ("math-bit",         ["number-of-1-bits", "counting-bits", "reverse-bits", "missing-number",
                          "power-of-two", "power-of-three", "power-of-four", "reordered-power"]),
]


def get_lc_tags(slug: str) -> tuple | None:
    """Call LC GraphQL API to get topic tags. Returns (bucket, topic) or None if failed."""
    query = """
    query getTopicTags($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            difficulty
            topicTags { slug }
        }
    }
    """
    try:
        resp = requests.post(
            "https://leetcode.com/graphql",
            json={"query": query, "variables": {"titleSlug": slug}},
            headers={
                "Content-Type": "application/json",
                "Referer": f"https://leetcode.com/problems/{slug}/",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
                "Origin": "https://leetcode.com",
            },
            timeout=10
        )
        if resp.status_code != 200:
            return None

        data = resp.json()
        q = data.get("data", {}).get("question")
        if not q:
            return None

        tags = [t["slug"] for t in q.get("topicTags", [])]

        # Map tags to topic — hard topics take priority
        hard_match = None
        easy_match = None
        for tag in tags:
            if tag in LC_TAG_TO_TOPIC:
                bucket, topic = LC_TAG_TO_TOPIC[tag]
                if bucket == "hard" and not hard_match:
                    hard_match = (bucket, topic)
                elif bucket == "easy" and not easy_match:
                    easy_match = (bucket, topic)

        # Refine dp-1d vs dp-2d based on difficulty
        result = hard_match or easy_match
        if result and result[1] == "dp-1d" and q.get("difficulty") == "Hard":
            result = ("hard", "dp-2d")

        return result or ("easy", "uncategorized")

    except Exception:
        return None


def classify_from_keywords(slug: str) -> tuple:
    """Keyword fallback classifier."""
    for topic, keywords in TOPIC_RULES:
        for kw in keywords:
            if kw in slug:
                bucket = "hard" if topic in HARD_TOPICS else "easy"
                return bucket, topic
    return "easy", "uncategorized"


def classify(slug: str, url: str) -> tuple:
    """Classify using LC API first, fall back to keywords."""
    lc_slug = url.split('/problems/')[-1].rstrip('/')
    result = get_lc_tags(lc_slug)
    if result:
        return result
    print(f"  ⚠️  API failed for {lc_slug}, using keyword fallback")
    return classify_from_keywords(slug)


def parse_readme(folder: Path) -> dict | None:
    readme = folder / "README.md"
    if not readme.exists():
        return None
    text = readme.read_text(errors='ignore')

    url_match = re.search(r'href="(https://leetcode\.com/problems/[^"]+)"', text)
    title_match = re.search(r'href="https://leetcode\.com/problems/[^"]+">(?:\d+\.\s+)?([^<]+)</a>', text)
    if not url_match or not title_match:
        return None

    folder_id_match = re.match(r'^(\d+)-', folder.name)
    problem_id = int(folder_id_match.group(1)) if folder_id_match else 0

    diff_match = re.search(r'Difficulty-(Easy|Medium|Hard)', text)
    if not diff_match:
        diff_match = re.search(r'<h3>(Easy|Medium|Hard)</h3>', text)

    url = url_match.group(1).rstrip('/')
    lc_slug = url.split('/problems/')[-1].rstrip('/')

    return {
        "id": problem_id,
        "title": title_match.group(1).strip(),
        "url": f"https://leetcode.com/problems/{lc_slug}/",
        "difficulty": diff_match.group(1) if diff_match else "Medium",
        "solved": True,
        "last_reviewed": None
    }


def url_to_slug(url: str) -> str:
    match = re.search(r'/problems/([^/]+)', url)
    return match.group(1).lower().rstrip('/') if match else ''


def get_problem_folders(repo_root: Path) -> list:
    skip = {'.git', '_dsa-scheduler', '.github'}
    return sorted(
        [f for f in repo_root.iterdir() if f.is_dir() and f.name not in skip],
        key=lambda f: f.name
    )


def update_problems_json(repo_root: Path):
    problems_path = repo_root / "_dsa-scheduler" / "problems.json"
    if not problems_path.exists():
        print(f"Error: {problems_path} not found")
        return

    with open(problems_path) as f:
        problems = json.load(f)

    # Build known slugs
    known_slugs = set()
    for bucket in ["hard", "easy"]:
        for topic, prob_list in problems[bucket].items():
            for prob in prob_list:
                known_slugs.add(url_to_slug(prob.get("url", "")))

    all_folders = get_problem_folders(repo_root)
    print(f"Found {len(all_folders)} problem folders in repo")

    # ── Step 1: Auto-discover new problems ───────────────────────────────────
    newly_added = []
    for folder in all_folders:
        raw_slug = folder.name.lower()
        lc_slug = re.sub(r'^\d+-', '', raw_slug)

        if lc_slug in known_slugs or raw_slug in known_slugs:
            continue
        if any(ks in lc_slug for ks in known_slugs if len(ks) > 10):
            continue

        meta = parse_readme(folder)
        if not meta:
            continue

        actual_slug = url_to_slug(meta["url"])
        if actual_slug in known_slugs:
            continue

        # Classify via LC API → keyword fallback
        bucket, topic = classify(lc_slug, meta["url"])

        problems[bucket].setdefault(topic, []).append(meta)
        if "uncategorized" not in problems.get(bucket, {}):
            problems.setdefault(bucket, {})["uncategorized"] = []

        known_slugs.add(actual_slug)
        newly_added.append(f"{meta['id'] or '?'}. {meta['title']} → {bucket}/{topic}")
        time.sleep(0.3)  # be polite to LC API

    if newly_added:
        print(f"\n{len(newly_added)} newly discovered:")
        for p in newly_added:
            print(f"  ➕ {p}")
    else:
        print("No new problems discovered.")

    # ── Step 2: Sync solved status ────────────────────────────────────────────
    folder_slugs = set()
    for folder in all_folders:
        raw = folder.name.lower()
        folder_slugs.add(raw)
        folder_slugs.add(re.sub(r'^\d+-', '', raw))

    newly_solved = []
    for bucket in ["hard", "easy"]:
        for topic, prob_list in problems[bucket].items():
            for prob in prob_list:
                was_solved = prob.get("solved", False)
                lc_slug = url_to_slug(prob.get("url", ""))
                is_solved = lc_slug in folder_slugs or any(lc_slug in s for s in folder_slugs)
                prob["solved"] = is_solved
                if is_solved and not was_solved:
                    newly_solved.append(f"{prob['id']}. {prob['title']}")

    if newly_solved:
        print(f"\n{len(newly_solved)} newly solved:")
        for p in newly_solved:
            print(f"  ✅ {p}")
    else:
        print("No change in solved status.")

    # ── Step 3: Save ──────────────────────────────────────────────────────────
    with open(problems_path, "w") as f:
        json.dump(problems, f, indent=2)

    # ── Step 4: Summary ───────────────────────────────────────────────────────
    print("\nCoverage summary:")
    total_solved = total = 0
    for bucket in ["hard", "easy"]:
        for topic, prob_list in problems[bucket].items():
            s = sum(1 for p in prob_list if p["solved"])
            t = len(prob_list)
            total_solved += s
            total += t
            print(f"  {topic}: {'✅' if s == t else f'{s}/{t}'}")
    print(f"\nOverall: {total_solved}/{total}")


if __name__ == "__main__":
    repo_root = Path(os.environ.get("GITHUB_WORKSPACE", "."))
    update_problems_json(repo_root)
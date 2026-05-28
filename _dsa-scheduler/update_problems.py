"""
Runs on every push to main via GitHub Actions.

Does two things:
1. AUTO-DISCOVER new problem folders not in problems.json → parse README → classify → add
2. SYNC solved status for all problems already in the bank
"""
import json
import os
import re
from pathlib import Path

# ── Topic classification by slug keywords ────────────────────────────────────
TOPIC_RULES = [
    # Hard topics first
    ("graphs-bfs-dfs",   ["island", "flood-fill", "clone-graph", "surrounded", "pacific", "atlantic",
                          "rotting", "word-ladder", "bipartite", "01-matrix", "treasure", "gates"]),
    ("graphs-topo-sort", ["course-schedule", "alien-dictionary", "sequence-reconstruction",
                          "parallel-courses", "minimum-height-trees"]),
    ("graphs-advanced",  ["network-delay", "cheapest-flights", "redundant-connection",
                          "connected-components", "min-cost-to-connect", "swim-in-rising", "valid-tree"]),
    ("trees",            ["binary-tree", "inorder", "preorder", "postorder", "level-order",
                          "serialize", "deserialize", "lowest-common-ancestor", "balanced-binary",
                          "invert-binary", "subtree", "diameter", "path-sum", "right-side-view",
                          "good-nodes", "kth-smallest-element-in-a-bst", "validate-binary",
                          "maximum-balanced-shipments"]),
    ("heaps",            ["median", "data-stream", "merge-k-sorted", "kth-largest", "kth-largest-element-in-a-stream",
                          "k-closest", "task-scheduler", "reorganize-string", "design-twitter",
                          "k-pairs", "stone-weight", "pass-ratio"]),
    ("sliding-window",   ["longest-substring-without", "sliding-window-maximum", "minimum-window",
                          "permutation-in-string", "repeating-character-replacement",
                          "erasure-value", "subarray-of-1s", "maximum-fruits-harvested",
                          "rearranging-fruits", "fruits-into-baskets"]),
    ("binary-search",    ["rotated-sorted-array", "minimum-in-rotated", "median-of-two",
                          "search-a-2d-matrix", "eating-bananas", "capacity-to-ship",
                          "peak-element", "time-based-key-value"]),
    ("backtracking",     ["combination-sum", "palindrome-partitioning", "letter-combinations",
                          "sudoku", "n-queens", "word-search", "permutations", "subsets"]),
    ("dp-1d",            ["climbing-stairs", "house-robber", "longest-increasing-subsequence",
                          "coin-change", "word-break", "target-sum", "longest-valid-parentheses",
                          "decode-ways"]),
    ("dp-2d",            ["longest-common-subsequence", "edit-distance", "coin-change-ii",
                          "count-square-submatrices", "burst-balloons", "regular-expression",
                          "pascals-triangle", "unique-paths", "minimum-path-sum",
                          "ways-to-express-an-integer"]),
    ("tries",            ["implement-trie", "prefix-tree", "add-and-search-words",
                          "word-search-ii", "replace-words", "maximum-xor"]),
    ("monotonic-stack",  ["largest-rectangle-in-histogram", "maximal-rectangle", "next-greater",
                          "daily-temperatures", "subarray-minimums", "asteroid"]),
    # Easy topics
    ("arrays",           ["two-sum", "buy-and-sell-stock", "product-of-array", "maximum-subarray",
                          "maximum-product-subarray", "container-with-most-water", "three-integer-sum",
                          "trapping-rain-water", "merge-intervals", "insert-interval", "gas-station",
                          "remove-one-element-to-make", "strictly-increasing", "rotate-array",
                          "move-zeroes", "best-time-to-buy"]),
    ("hashmaps",         ["group-anagrams", "anagram-groups", "longest-consecutive",
                          "subarray-sum-equals", "top-k-frequent", "lru-cache"]),
    ("strings",          ["valid-palindrome", "is-palindrome", "valid-anagram", "is-anagram",
                          "encode-and-decode", "string-encode", "longest-palindromic",
                          "palindromic-substrings", "add-strings", "reverse-string"]),
    ("stack-queue",      ["min-stack", "minimum-stack", "implement-queue", "implement-stack",
                          "evaluate-reverse-polish", "generate-parentheses", "car-fleet",
                          "validate-parentheses"]),
    ("linked-list",      ["reverse-linked-list", "reverse-a-linked-list", "merge-two-sorted-list",
                          "linked-list-cycle", "remove-nth-node", "remove-node-from-end",
                          "reorder-list", "reorder-linked", "add-two-numbers",
                          "reverse-nodes-in-k", "copy-list-with-random",
                          "copy-linked-list-with-random",
                          "convert-binary-number-in-a-linked-list"]),
    ("sorting",          ["sort-colors", "sort-list", "largest-number", "wiggle-sort", "sort-array",
                          "sort-matrix"]),
    ("greedy",           ["assign-cookies", "non-overlapping-intervals", "partition-labels",
                          "valid-parenthesis-string", "maximum-events", "matching-players",
                          "maximum-matching"]),
    ("math-bit",         ["number-of-1-bits", "counting-bits", "reverse-bits", "missing-number",
                          "sum-of-two-integers", "reverse-integer", "powx-n", "power-of-two",
                          "power-of-three", "power-of-four", "reordered-power-of-2",
                          "single-number", "hamming-distance", "range-product-queries"]),
]

HARD_TOPICS = {"graphs-bfs-dfs", "graphs-topo-sort", "graphs-advanced", "trees",
               "heaps", "sliding-window", "binary-search", "backtracking",
               "dp-1d", "dp-2d", "tries", "monotonic-stack"}


def classify_slug(slug: str) -> tuple:
    for topic, keywords in TOPIC_RULES:
        for kw in keywords:
            if kw in slug:
                bucket = "hard" if topic in HARD_TOPICS else "easy"
                return bucket, topic
    return "easy", "uncategorized"


def parse_readme(folder: Path) -> dict | None:
    readme = folder / "README.md"
    if not readme.exists():
        return None

    text = readme.read_text(errors='ignore')

    # Extract LC URL
    url_match = re.search(r'href="(https://leetcode\.com/problems/[^"]+)"', text)
    if not url_match:
        return None

    # Extract title — strip leading "NNNN. " if present (NeetCode uses its own IDs)
    title_match = re.search(r'href="https://leetcode\.com/problems/[^"]+">(?:\d+\.\s+)?([^<]+)</a>', text)
    if not title_match:
        return None
    title = title_match.group(1).strip()

    # Get LC problem ID from folder name prefix (most reliable source)
    folder_id_match = re.match(r'^(\d+)-', folder.name)
    problem_id = int(folder_id_match.group(1)) if folder_id_match else 0

    # Extract difficulty from badge or h3
    diff_match = re.search(r'Difficulty-(Easy|Medium|Hard)', text)
    if not diff_match:
        diff_match = re.search(r'<h3>(Easy|Medium|Hard)</h3>', text)

    url = url_match.group(1).rstrip('/')
    lc_slug = url.split('/problems/')[-1].rstrip('/')

    return {
        "id": problem_id,
        "title": title,
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

    # Build set of all known LC slugs
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
        # Get LC slug: strip leading digits from folder name
        raw_slug = folder.name.lower()
        lc_slug = re.sub(r'^\d+-', '', raw_slug)

        # Skip if already known (check both folder slug and lc slug)
        if lc_slug in known_slugs or raw_slug in known_slugs:
            continue
        # Also skip if any known slug is contained in this slug (duplicate folder)
        if any(ks in lc_slug for ks in known_slugs if len(ks) > 10):
            continue

        meta = parse_readme(folder)
        if not meta:
            continue

        actual_slug = url_to_slug(meta["url"])
        if actual_slug in known_slugs:
            continue

        bucket, topic = classify_slug(lc_slug)
        if "uncategorized" not in problems.get(bucket, {}):
            problems.setdefault(bucket, {})["uncategorized"] = []
        problems[bucket].setdefault(topic, []).append(meta)
        known_slugs.add(actual_slug)
        newly_added.append(f"{meta['id'] or '?'}. {meta['title']} → {bucket}/{topic}")

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
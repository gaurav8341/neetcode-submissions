"""
Runs on every push to main via GitHub Actions.

1. AUTO-DISCOVER new problem folders not in problems.json
   → calls LeetCode GraphQL API to get topic tags
   → maps tags using priority-based classifier (specific beats generic)
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

# ── LC tag → (bucket, topic, priority) ───────────────────────────────────────
# Lower priority number = more specific = wins over generic tags
# e.g. topological-sort (p=1) beats graph (p=5)
LC_TAG_MAP = {
    # Priority 1 — highly specific, always wins
    "topological-sort":  ("hard", "graphs-topo-sort", 1),
    "trie":              ("hard", "tries",            1),
    "monotonic-stack":   ("hard", "monotonic-stack",  1),
    "sliding-window":    ("hard", "sliding-window",   1),
    "backtracking":      ("hard", "backtracking",     1),
    "union-find":        ("hard", "graphs-advanced",  1),
    "shortest-path":     ("hard", "graphs-advanced",  1),

    # Priority 2 — specific
    "dynamic-programming": ("hard", "dp-1d",          2),
    "binary-search":       ("hard", "binary-search",  2),
    "heap-priority-queue": ("hard", "heaps",          2),
    "divide-and-conquer":  ("hard", "binary-search",  2),
    "recursion":           ("hard", "backtracking",   2),

    # Priority 3 — structural
    "tree":              ("hard", "trees",            3),
    "binary-tree":       ("hard", "trees",            3),
    "binary-search-tree":("hard", "trees",            3),
    "linked-list":       ("easy", "linked-list",      3),
    "stack":             ("easy", "stack-queue",      3),
    "queue":             ("easy", "stack-queue",      3),
    "monotonic-queue":   ("easy", "stack-queue",      3),

    # Priority 4 — algorithmic
    "depth-first-search":  ("hard", "graphs-bfs-dfs", 4),
    "breadth-first-search":("hard", "graphs-bfs-dfs", 4),
    "matrix":              ("hard", "graphs-bfs-dfs", 4),
    "sorting":             ("easy", "sorting",         4),
    "counting-sort":       ("easy", "sorting",         4),
    "greedy":              ("easy", "greedy",          4),
    "bit-manipulation":    ("easy", "math-bit",        4),
    "two-pointers":        ("easy", "arrays",          4),
    "prefix-sum":          ("easy", "arrays",          4),
    "string-matching":     ("easy", "strings",         4),

    # Priority 5 — generic, loses to everything above
    "graph":             ("hard", "graphs-bfs-dfs",  5),
    "array":             ("easy", "arrays",           5),
    "hash-table":        ("easy", "hashmaps",         5),
    "string":            ("easy", "strings",          5),
    "math":              ("easy", "math-bit",         5),
    "number-theory":     ("easy", "math-bit",         5),
}

HARD_TOPICS = {"graphs-bfs-dfs", "graphs-topo-sort", "graphs-advanced", "trees",
               "heaps", "sliding-window", "binary-search", "backtracking",
               "dp-1d", "dp-2d", "tries", "monotonic-stack"}


def classify_from_tags(tags: list, difficulty: str) -> tuple:
    """
    Priority-based classifier — most specific tag wins.
    Hard topics always beat easy topics at same priority.
    dp-1d → dp-2d upgrade for Hard difficulty.
    """
    best = None
    best_priority = 999

    for tag in tags:
        if tag not in LC_TAG_MAP:
            continue
        bucket, topic, priority = LC_TAG_MAP[tag]
        # Hard topics beat easy at same priority level
        if priority < best_priority or (
            priority == best_priority and bucket == "hard" and best and best[0] == "easy"
        ):
            best = (bucket, topic)
            best_priority = priority

    if not best:
        return ("easy", "uncategorized")

    # Upgrade dp-1d → dp-2d for Hard problems
    if best == ("hard", "dp-1d") and difficulty == "Hard":
        return ("hard", "dp-2d")

    return best


def get_lc_classification(lc_slug: str) -> tuple | None:
    query = """
    query($t: String!) {
        question(titleSlug: $t) {
            difficulty
            topicTags { slug }
        }
    }
    """
    try:
        resp = requests.post(
            "https://leetcode.com/graphql",
            json={"query": query, "variables": {"t": lc_slug}},
            headers={
                "Content-Type": "application/json",
                "Referer": f"https://leetcode.com/problems/{lc_slug}/",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
                "Origin": "https://leetcode.com",
            },
            timeout=10
        )
        if resp.status_code != 200:
            return None
        q = resp.json().get("data", {}).get("question")
        if not q:
            return None
        tags = [t["slug"] for t in q.get("topicTags", [])]
        difficulty = q.get("difficulty", "Medium")
        return classify_from_tags(tags, difficulty)
    except Exception:
        return None


def parse_readme(folder: Path) -> dict | None:
    readme = folder / "README.md"
    if not readme.exists():
        return None
    text = readme.read_text(errors='ignore')
    url_match = re.search(r'href="(https://leetcode\.com/problems/[^"]+)"', text)
    title_match = re.search(
        r'href="https://leetcode\.com/problems/[^"]+">(?:\d+\.\s+)?([^<]+)</a>', text)
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

    known_slugs = set()
    for bucket in ["hard", "easy"]:
        for topic, prob_list in problems[bucket].items():
            for prob in prob_list:
                known_slugs.add(url_to_slug(prob.get("url", "")))

    all_folders = get_problem_folders(repo_root)
    print(f"Found {len(all_folders)} problem folders in repo")

    # ── Step 1: Auto-discover ─────────────────────────────────────────────────
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
        result = get_lc_classification(actual_slug)
        time.sleep(0.3)
        bucket, topic = result if result else ("easy", "uncategorized")
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
                is_solved = lc_slug in folder_slugs or any(
                    lc_slug in s for s in folder_slugs)
                prob["solved"] = is_solved
                if is_solved and not was_solved:
                    newly_solved.append(f"{prob['id']}. {prob['title']}")

    if newly_solved:
        print(f"\n{len(newly_solved)} newly solved:")
        for p in newly_solved:
            print(f"  ✅ {p}")
    else:
        print("No change in solved status.")

    with open(problems_path, "w") as f:
        json.dump(problems, f, indent=2)

    print("\nCoverage summary:")
    total_solved = total = 0
    for bucket in ["hard", "easy"]:
        for topic, prob_list in problems[bucket].items():
            if not prob_list:
                continue
            s = sum(1 for p in prob_list if p["solved"])
            t = len(prob_list)
            total_solved += s
            total += t
            print(f"  {bucket}/{topic}: {'✅' if s == t else f'{s}/{t}'}")
    print(f"\nOverall: {total_solved}/{total}")


if __name__ == "__main__":
    repo_root = Path(os.environ.get("GITHUB_WORKSPACE", "."))
    update_problems_json(repo_root)
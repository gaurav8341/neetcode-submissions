"""
One-time script: reclassify ALL problems in problems.json using
priority-based LC API classifier. Run via GitHub Actions.
"""
import json, re, time, requests
from pathlib import Path

LC_TAG_MAP = {
    "topological-sort":    ("hard", "graphs-topo-sort", 1),
    "trie":                ("hard", "tries",            1),
    "monotonic-stack":     ("hard", "monotonic-stack",  1),
    "sliding-window":      ("hard", "sliding-window",   1),
    "backtracking":        ("hard", "backtracking",     1),
    "union-find":          ("hard", "graphs-advanced",  1),
    "shortest-path":       ("hard", "graphs-advanced",  1),
    "dynamic-programming": ("hard", "dp-1d",            2),
    "binary-search":       ("hard", "binary-search",    2),
    "heap-priority-queue": ("hard", "heaps",            2),
    "divide-and-conquer":  ("hard", "binary-search",    2),
    "recursion":           ("hard", "backtracking",     2),
    "tree":                ("hard", "trees",            3),
    "binary-tree":         ("hard", "trees",            3),
    "binary-search-tree":  ("hard", "trees",            3),
    "linked-list":         ("easy", "linked-list",      3),
    "stack":               ("easy", "stack-queue",      3),
    "queue":               ("easy", "stack-queue",      3),
    "depth-first-search":  ("hard", "graphs-bfs-dfs",   4),
    "breadth-first-search":("hard", "graphs-bfs-dfs",   4),
    "matrix":              ("hard", "graphs-bfs-dfs",   4),
    "sorting":             ("easy", "sorting",          4),
    "greedy":              ("easy", "greedy",           4),
    "bit-manipulation":    ("easy", "math-bit",         4),
    "two-pointers":        ("easy", "arrays",           4),
    "prefix-sum":          ("easy", "arrays",           4),
    "graph":               ("hard", "graphs-bfs-dfs",   5),
    "array":               ("easy", "arrays",           5),
    "hash-table":          ("easy", "hashmaps",         5),
    "string":              ("easy", "strings",          5),
    "math":                ("easy", "math-bit",         5),
}

def classify(tags, difficulty):
    best, best_p = None, 999
    for tag in tags:
        if tag not in LC_TAG_MAP: continue
        b, t, p = LC_TAG_MAP[tag]
        if p < best_p or (p == best_p and b == "hard" and best and best[0] == "easy"):
            best, best_p = (b, t), p
    if not best: return ("easy", "uncategorized")
    if best == ("hard", "dp-1d") and difficulty == "Hard":
        return ("hard", "dp-2d")
    return best

def get_lc(slug):
    try:
        r = requests.post("https://leetcode.com/graphql",
            json={"query":"query($t:String!){question(titleSlug:$t){difficulty topicTags{slug}}}",
                  "variables":{"t":slug}},
            headers={"Content-Type":"application/json",
                     "Referer":f"https://leetcode.com/problems/{slug}/",
                     "User-Agent":"Mozilla/5.0","Origin":"https://leetcode.com"},
            timeout=10)
        if r.status_code != 200: return None
        q = r.json().get("data",{}).get("question")
        if not q: return None
        return classify([t["slug"] for t in q.get("topicTags",[])], q.get("difficulty","Medium"))
    except: return None

def url_slug(url):
    m = re.search(r'/problems/([^/]+)', url)
    return m.group(1).rstrip('/') if m else ''

path = Path("_dsa-scheduler/problems.json")
with open(path) as f: data = json.load(f)

all_probs = [(b,t,p) for b in ["hard","easy"] for t,ps in data[b].items() for p in ps]
print(f"Reclassifying {len(all_probs)} problems via LC API (priority-based)...")

TOPICS_HARD = ["graphs-bfs-dfs","graphs-topo-sort","graphs-advanced","trees",
               "heaps","sliding-window","binary-search","backtracking",
               "dp-1d","dp-2d","tries","monotonic-stack"]
TOPICS_EASY = ["arrays","hashmaps","strings","stack-queue",
               "linked-list","sorting","greedy","math-bit","uncategorized"]

new_data = {"hard":{t:[] for t in TOPICS_HARD}, "easy":{t:[] for t in TOPICS_EASY}}
moved = 0

for i, (old_b, old_t, prob) in enumerate(all_probs):
    slug = url_slug(prob.get("url",""))
    result = get_lc(slug) if slug else None
    time.sleep(0.3)
    nb, nt = result if result else (old_b, old_t)
    new_data[nb].setdefault(nt,[]).append(prob)
    if nb != old_b or nt != old_t:
        moved += 1
        print(f"  🔄 {prob.get('title')} → {nb}/{nt}")
    if (i+1) % 20 == 0:
        print(f"  Progress: {i+1}/{len(all_probs)}...")

with open(path,"w") as f: json.dump(new_data, f, indent=2)
print(f"\nDone. {moved} reclassified.")
for b in ["hard","easy"]:
    for t, ps in new_data[b].items():
        if ps:
            s = sum(1 for p in ps if p["solved"])
            print(f"  {b}/{t}: {s}/{len(ps)}")
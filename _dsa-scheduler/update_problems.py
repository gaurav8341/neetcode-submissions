"""
Runs on every push to main via GitHub Actions.
Reads all root-level folder slugs, matches against leetcode URL
slugs in problems.json. Zero hardcoding — fully automatic.
"""
import json
import os
import re
from pathlib import Path


def get_solved_slugs(repo_root: Path) -> set:
    """Collect all problem folder slugs from root level."""
    skip = {'.git', '_dsa-scheduler', '.github'}
    slugs = set()
    for folder in repo_root.iterdir():
        if folder.is_dir() and folder.name not in skip:
            slugs.add(folder.name.lower())
    print(f"Found {len(slugs)} solved problem folders")
    return slugs


def url_to_slug(url: str) -> str:
    """Extract slug from leetcode URL.
    https://leetcode.com/problems/number-of-islands/ -> number-of-islands
    """
    match = re.search(r'/problems/([^/]+)', url)
    return match.group(1).lower() if match else ''


def update_problems_json(repo_root: Path):
    problems_path = repo_root / "_dsa-scheduler" / "problems.json"
    if not problems_path.exists():
        print(f"Error: {problems_path} not found")
        return

    with open(problems_path) as f:
        problems = json.load(f)

    solved_slugs = get_solved_slugs(repo_root)
    newly_solved = []

    for bucket in ["hard", "easy"]:
        for topic, prob_list in problems[bucket].items():
            for prob in prob_list:
                was_solved = prob.get("solved", False)
                lc_slug = url_to_slug(prob.get("url", ""))
                is_solved = lc_slug in solved_slugs or any(
                    lc_slug in s for s in solved_slugs
                )
                prob["solved"] = is_solved
                if is_solved and not was_solved:
                    newly_solved.append(f"{prob['id']}. {prob['title']}")

    with open(problems_path, "w") as f:
        json.dump(problems, f, indent=2)

    if newly_solved:
        print(f"\n{len(newly_solved)} newly solved:")
        for p in newly_solved:
            print(f"  ✅ {p}")
    else:
        print("No new problems solved since last run.")

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

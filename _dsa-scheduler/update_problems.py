"""
Runs on every push to main via GitHub Actions.
Reads folder names from Data Structures & Algorithms/,
extracts the slug, and matches against the leetcode URL in problems.json.

Zero hardcoding — works automatically for any new problem NeetCode pushes.
"""
import json
import os
import re
from pathlib import Path


def get_solved_slugs(repo_root: Path) -> set:
    """Collect all folder slugs from the repo."""
    slugs = set()

    dsa_folder = repo_root
    if dsa_folder.exists():
        for folder in dsa_folder.iterdir():
            if folder.is_dir():
                slugs.add(folder.name.lower())

    # Root level folders (e.g. 542-01-matrix)
    skip = {'.git', 'dsa-scheduler', '.github', 'Data Structures & Algorithms'}
    for folder in repo_root.iterdir():
        if folder.is_dir() and folder.name not in skip:
            slugs.add(folder.name.lower())

    return slugs


def url_to_slug(url: str) -> str:
    """Extract slug from leetcode URL.
    https://leetcode.com/problems/number-of-islands/ -> number-of-islands
    """
    match = re.search(r'/problems/([^/]+)', url)
    return match.group(1).lower() if match else ''


def update_problems_json(repo_root: Path):
    problems_path = repo_root / "dsa-scheduler" / "problems.json"
    if not problems_path.exists():
        print(f"Error: {problems_path} not found")
        return

    with open(problems_path) as f:
        problems = json.load(f)

    solved_slugs = get_solved_slugs(repo_root)
    print(f"Found {len(solved_slugs)} solved folders in repo")

    newly_solved = []

    for bucket in ["hard", "easy"]:
        for topic, prob_list in problems[bucket].items():
            for prob in prob_list:
                was_solved = prob.get("solved", False)

                # Extract slug from the problem's leetcode URL
                lc_slug = url_to_slug(prob.get("url", ""))

                # Match: either exact slug match or folder contains the slug
                is_solved = lc_slug in solved_slugs or any(
                    lc_slug in folder_slug
                    for folder_slug in solved_slugs
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
        print("No newly solved problems since last run.")

    # Print summary
    print("\nCoverage summary:")
    total_solved = total = 0
    for bucket in ["hard", "easy"]:
        for topic, prob_list in problems[bucket].items():
            s = sum(1 for p in prob_list if p["solved"])
            t = len(prob_list)
            total_solved += s
            total += t
            bar = "✅" if s == t else f"{s}/{t}"
            print(f"  {topic}: {bar}")
    print(f"\nOverall: {total_solved}/{total}")


if __name__ == "__main__":
    repo_root = Path(os.environ.get("GITHUB_WORKSPACE", "."))
    update_problems_json(repo_root)


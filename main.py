import argparse
from toolkit.github_api import get_repo
from toolkit.display import display_repo

def main():
    parser = argparse.ArgumentParser(description="Developer Utility Toolkit")
    subparsers = parser.add_subparsers(dest="command", required=True)
    repo_parser = subparsers.add_parser("repo", help="Get github repo information.")
args = parser.parse_args()
owner = args.owner.strip()
repo = args.repo.strip()
if not owner or not repo:
    parser.error("Both owner and repository name are required.")
data = get_repo(owner,repo)

display_repo(data)
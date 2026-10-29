import argparse
from toolkit.github_api import get_repo
from toolkit.display import display_repo

parser = argparse.ArgumentParser()
parser.add_argument("owner")
parser.add_argument("repo")
args = parser.parse_args()
owner = args.owner.strip()
repo = args.repo.strip()
if not owner or not repo:
    parser.error("Both owner and repository name are required.")
data = get_repo(owner,repo)

display_repo(data)
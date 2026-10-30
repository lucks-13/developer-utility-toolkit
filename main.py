import argparse
from toolkit.github_api import get_repo
from toolkit.github_user import get_user
from toolkit.compare import compare_repos
from toolkit.display import display_repo, display_user, display_comparison

def main():
    parser = argparse.ArgumentParser(description="Developer Utility Toolkit")
    subparsers = parser.add_subparsers(dest="command", required=True)
    repo_parser = subparsers.add_parser("repo", help="Get github repo information.")
    repo_parser.add_argument("owner", help="Github username or organization name")
    repo_parser.add_argument("repo", help="Name of the github repo")

    user_parser = subparsers.add_parser("user",help="Get Github user information.")
    user_parser.add_argument("username",help="Github username")

    args = parser.parse_args()
    if args.command == "repo":
        owner = args.owner.strip()
        repo = args.repo.strip()
        if not owner or not repo:
            parser.error("Both owner and repository name are required.")
        data = get_repo(owner,repo)
        display_repo(data)

    elif args.command == "user":
        username = args.username.strip()

        if not username:
            parser.error("Github username  is required.")

        data = get_user(username)
        display_user(data)

if __name__ == "__main__":
    main()
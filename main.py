import argparse
from toolkit.github_api import get_repo
from toolkit.github_user import get_user
from toolkit.compare import compare_repos
from toolkit.display import display_repo, display_user, display_comparison, display_search_results
from toolkit.github_search import search_repos
from toolkit.export import export_csv, export_json

def main():
    parser = argparse.ArgumentParser(description="Developer Utility Toolkit")
    subparsers = parser.add_subparsers(dest="command", required=True)
    repo_parser = subparsers.add_parser("repo", help="Get github repo information.")
    repo_parser.add_argument("owner", help="Github username or organization name")
    repo_parser.add_argument("repo", help="Name of the github repo")
    repo_parser.add_argument("--export", choices=["csv","json"], help="Export results as CSV or Json")

    user_parser = subparsers.add_parser("user",help="Get Github user information.")
    user_parser.add_argument("username",help="Github username")
    user_parser.add_argument("--export", choices=["csv","json"], help="Export results as CSV or Json")

    compare_parser = subparsers.add_parser("compare", help="Compare two github repos.")
    compare_parser.add_argument("owner1")
    compare_parser.add_argument("repo1")
    compare_parser.add_argument("owner2")
    compare_parser.add_argument("repo2")
    compare_parser.add_argument("--export", choices=["csv","json"], help="Export results as CSV or Json")

    search_parser = subparsers.add_parser("search", help="Search github repo")
    search_parser.add_argument("query")
    search_parser.add_argument("--language", help="Filter repo by programming language.")
    search_parser.add_argument("--limit", type=int, default=5)
    search_parser.add_argument("--export", choices=["csv","json"], help="Export results as CSV or Json")

    args = parser.parse_args()
    if args.command == "repo":
        owner = args.owner.strip()
        repo = args.repo.strip()

        if not owner or not repo:
            parser.error("Both owner and repository name are required.")
        
        data = get_repo(owner,repo)
        display_repo(data)

        if args.export == "csv":
            export_json(data, f"{repo}.csv")
        elif args.export == "json":
            export_json(data, f"{repo}.json")
    

    elif args.command == "user":
        username = args.username.strip()

        if not username:
            parser.error("Github username  is required.")

        data = get_user(username)
        display_user(data)

        if args.export == "csv":
            export_json(data, f"{repo}.csv")
        elif args.export == "json":
            export_json(data, f"{repo}.json")

    elif args.command == "compare":
        owner1 = args.owner1.strip()
        repo1 = args.repo1.strip()
        owner2 = args.owner2.strip()
        repo2 = args.repo2.strip()

        if not all([owner1, repo1, owner2, repo2]):
            parser.error("All repo details are required.")
        data1 = get_repo(owner1, repo1)
        data2 = get_repo(owner2, repo2)
        comparison = compare_repos(data1, data2)
        display_comparison(comparison)

        if args.export == "csv":
            export_json(data, "comparison.csv")
        elif args.export == "json":
            export_json(data, "comparison.json")

    elif args.command == "search":
        query = args.query.strip()
        if not query:
            parser.error("Search query is required.")
        if args.limit < 1 or args.limit > 100:
            parser.error("Limit must be between 1 and 100.")
        language = args.language.strip() if args.language else None
        if language == "":
            parser.error("Language cannot be empty.")
        data = search_repos(query,language,args.limit)
        display_search_results(data)

if __name__ == "__main__":
    main()
def compare_repos(repo1, repo2):
    if repo1 is None or repo2 is None:
        print("Unable to compare repo, Repo data is missing.")
        return None
    comparison = {
        "Repository" : [
            repo1.get("Repository", "Not Available"),
            repo2.get("Repository", "Not Available")
        ],
        "Owner" : [
            repo1.get("Owner", "Not Available"),
            repo2.get("Owner", "Not Available")
        ],
        "Language" : [
            
        ],
    }
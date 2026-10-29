import requests
import argparse

def get_repo(owner, repo):
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        data_dict = {
            "Repository" : data["name"] or "Not Available",
            "Owner" : data["owner"]["login"] or "Not Available",
            "Description" : data["description"] or "Not Available",
            "Language" : data["language"] or "Not Available",
            "Stars" : data["stargazers_count"] if data["stargazers_count"] is not None else "Not Available",
            "Forks" : data["forks_count"] if data["forks_count"] is not None else "Not Available",
            "URL" : data["html_url"] or "Not Available"
        }
        return data_dict
    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            print("The repo you are looking is not found.")
        elif response.status_code == 403:
            print("The request was forbidden.")
        else:
            print(f"Github API error : {response.status_code}.")
        return None
    except requests.exceptions.ConnectionError:
        print("Unable to connect Github.")
        return None
    except requests.exceptions.Timeout:
        print("The request timed out.")
        return None
    
parser = argparse.ArgumentParser()
parser.add_argument("owner")
parser.add_argument("repo")
args = parser.parse_args()
owner = args.owner
repo = args.repo
if not owner or not repo:
    parser.error("Both owner and repository name are required.")
data = get_repo(owner,repo)

if data is not None:
    print("\n=============================")
    print("     Github Repository       ")
    print("=============================")
    for key,value in data.items():
        print(f"{key} : {value}")
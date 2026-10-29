import requests

def get_repo(owner, repo):
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        data_dict = {
            "Repository" : data["name"],
            "Owner" : data["owner"]["login"],
            "Description" : data["description"],
            "Language" : data["language"],
            "Stars" : data["stargazers_count"],
            "Forks" : data["forks_count"],
            "URL" : data["html_url"]
        }
        return data_dict
    except requests.exceptions.HTTPError:
         print("Github returned an HTTP error.")
         return None
    except requests.exceptions.ConnectionError:
         print("Unable to connect Github.")
         return None
    except requests.exceptions.Timeout:
         print("The request timed out.")
         return None
while True:
    try:
        owner = input("Enter GitHub Username or Organiztion name : ").strip()
        repo = input("Enter repository name : ").strip()
        if not owner or not repo:
            continue
        else:
            break
    except ValueError:
        continue
data = get_repo(owner,repo)

if data is not None:
    for key,value in data.items():
        print(f"{key} : {value}")
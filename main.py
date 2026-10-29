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
         
data = get_repo("python","cpython")

for k,v in data.items():
        print(f"{k} : {v}")
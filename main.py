import requests

def get_repo(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)
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
data = get_repo("python","cpython")

for k,v in data.items():
        print(f"{k} : {v}")
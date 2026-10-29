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
        "Stars" : data["star"]

    }
    return data_dict
data = get_repo("python","cpython")
print(data)

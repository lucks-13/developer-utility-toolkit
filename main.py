import requests

def get_repo(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)
    data = response.json()
    return data
data = get_repo("python","cpython")
print(data)

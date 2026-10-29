import requests

def get_repo(owner,repo):
    url = 

response = requests.get("https://api.github.com/repos/python/cpython")
print(response.status_code)
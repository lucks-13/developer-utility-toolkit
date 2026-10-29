import requests

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
            "URL" : data["html_url"] or "Not Available",
            "Watchers" : data["watchers_count"],
            "Open Issues" : data["open_issues_count"],
            "Default Branch" : data["default_branch"] or "Not Available",
            "License" : (data["license"]["spdx_id"] if data["license"] is not None else "Not Available"),
            "Size (KB)" : data["size"],
            "Created At" : data["created_at"],
            "Topics" : ", ".join(data["topics"]) if data["topics"] else "None",
            "Archived" : data["archived"],
            "Is Fork" : data["fork"]
        }
        return data_dict
    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            print("The repository not found.")
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
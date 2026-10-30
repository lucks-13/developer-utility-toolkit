import requests

def get_user(username):
    try:
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        user_data = {
            "Username" : data.get("login") or "Not Available",
            "Name" : data.get("name") or "Not Available",
            "Bio" : data.get("bio") or "Not Available",
            "Location" : data.get("location") or "Not Available",
            "Company" : data.get("company") or "Not Available",
            "Public Repos" : data.get("public_repos",0),
            "Followers" : data.get("followers",0),
            "Following" : data.get("following",0),
            "Account Type" : data.get("type") or "Not Available",
            "Created At" : data.get("created_at") or "Not Available",
            "Profile URL" : data.get("html_url") or "Not Available"
        }

        return user_data
    
    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            print("Github user not found.")
        elif response.status_code == 403:
            print("The request was forbidden.")
        else:
            print(f"Github API error : {response.status_code}.")
        
        return None

    

    
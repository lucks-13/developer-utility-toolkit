import requests

def get_user(username):
    try:
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        user_data{
            "Username" : data.get("login") or "Not Available",
            "Name" : data.get("name") or "Not Available",
            ""
        }
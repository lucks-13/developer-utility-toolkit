import requests

def get_user(username):
    try:
        url = f"https://api.github.com/users/{username}"
        res
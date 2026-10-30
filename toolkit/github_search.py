import requests

def search_repos(query, language=None, limit=5):
    try:
        url = "https://api.github.com/search/repositories"
        search_query = query
        if language:
            search_query += f" language:{language}"
        params = {
            "q" : 
        }
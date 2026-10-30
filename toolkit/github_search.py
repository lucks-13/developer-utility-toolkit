import requests

def search_repos(query, language=None, limit=5):
    try:
        url = "https://api.github.com/search/repositories"
        search_query = query
        if language:
            search_query += f" language:{language}"
        params = {
            "q" : search_query,
            "sort" : "stars",
            "order" : "desc",
            "per_page" : limit
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
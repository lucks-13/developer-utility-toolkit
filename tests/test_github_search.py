import requests

from unittest.mock import Mock, patch
from toolkit.github_search import search_repos

@patch("toolkit.github_search.requests.get")
def 
"""Any form of extras that were not listed in the docs to make your life simpler."""

import requests
from .models.model import *
from .search import get_maps_from_search
from .search import SortOrder

def get_user_from_username(username:str) -> UserDetail:
    """Returns a `UserDetail` object from a username, or None if the user could not be foumd."""
    results = get_maps_from_search(page=0, sortOrder="Relevance", q=username)
    return results.user
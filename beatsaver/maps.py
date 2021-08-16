"""All form of requests involving maps."""

import requests
from .models.model import *

base_url = "https://beatsaver.com/api"

def get_map_from_id(id:str) -> MapDetail:
    """Returns a `MapDetail` object, or None if the map has been deleted / does not exist."""
    r = requests.get(f'{base_url}/maps/id/{id}')
    if r.status_code == 404:
        return None

    details = MapDetail(**r.json())

    return details

def get_map_from_hash(hash:str) -> MapDetail:
    """Returns a `MapDetail` object, or None if the map has been deleted / does not exist."""
    r = requests.get(f'{base_url}/maps/hash/{hash}')
    if r.status_code == 404:
        return None
    details = MapDetail(**r.json())
    return details

def get_maps_from_user(id:int, page:int=0) -> SearchResponse:
    """Returns a `SearchResponse` object, or None if the user does not exist."""
    r = requests.get(f'{base_url}/maps/uploader/{id}/{page}')
    if r.status_code == 404:
        return None
    details = SearchResponse(**r.json())

    return details

def get_latest_maps(automapper:bool, before:str='') -> SearchResponse:
    """Returns a `SearchResponse` object, or None if no maps could be found.
    :param: automapper  Whether it should include automapped songs.
    :param: before      Only include maps before certain date (YYYY-MM-DDTHH:MM:SS+00:00)"""
    bopt = f"&before={before}" if before != '' else '' 
    r = requests.get(f'{base_url}/maps/latest?automapper={str(automapper).lower()}{bopt}')
    
    details = SearchResponse(**r.json())

    return details

def get_most_played_maps(page:int=0) -> SearchResponse:
    """Returns a `SearchResponse` object"""
    r = requests.get(f'{base_url}/maps/plays/{page}')

    details = SearchResponse(**r.json())
    return details
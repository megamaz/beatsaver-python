"""All form of requests involving maps."""

import requests
from typing import Literal
from .models.models import *
from .models.exceptions import *
from urllib.parse import urlencode
base_url = "https://beatsaver.com/api"
_r = requests.Session()

def get_map_from_id(id: str) -> MapDetail:
    """Returns a `MapDetail` object containing the requested map info. If the map was not found, raises `BeatSaverNotFoundException`.
    Do note that the behavior of this endpoint does not match the behavior of the website. If the map is unpublished, this endpoint will return the map details, but the website will redirect to the home page."""
    response = _r.get(f'{base_url}/maps/id/{id}')
    if response.status_code == 404:
        raise BeatSaverNotFoundException(f"Error response: {response.json()['error']}")

    details = MapDetail(**response.json())

    return details


def get_maps_from_ids(*ids: str) -> dict[str, MapDetail]:
    """Returns a dict of `MapDetail` objects, where the keys are the IDs and the value is the `MapDetail`. If the ID does not exist, then it will not be placed in the dictionary. If none of the IDs exist, then the dictionary will be empty."""
    result = {}
    response = _r.get(f'{base_url}/maps/ids/{",".join(ids)}')
    for m in response.json():
        result[m] = MapDetail(**response.json()[m])

    return result


def get_map_from_hash(hash: str) -> MapDetail:
    """Returns a `MapDetail` object containing the requested map info. If the map was not found, raises `BeatSaverNotFoundException`.
    Do note that the behavior of this endpoint does not match the behavior of the website. If the map is unpublished, this endpoint will return the map details, but the website will redirect to the home page."""
    response = _r.get(f'{base_url}/maps/hash/{hash}')
    if response.status_code == 404:
        raise BeatSaverNotFoundException(f"Error response: {response.json()['error']}")
    
    details = MapDetail(**response.json())
    return details


def get_maps_from_user(id: int, page: int = 0, includeCollabs:bool=False) -> SearchResponse:
    """Returns a `SearchResponse` object containing maps released by a user. Raises `BeatSaverNotFoundException` if no maps could be found.
    :param: includeCollabs      If true, this will also search for maps where the user is added as a collaborator."""
    if includeCollabs:
        response = _r.get(f'{base_url}/maps/collborations/{id}')
    else:
        response = _r.get(f'{base_url}/maps/uploader/{id}/{page}')
    if response.status_code == 400:
        raise BeatSaverArgumentException(f"Error response: {response.json()['error']}")
    
    details = SearchResponse(**response.json())
    if len(details.docs) == 0:
        raise BeatSaverNotFoundException("No maps with the requested user ID could be found.")
    
    return details

def get_latest_maps(after: str = '', 
                    automapper: bool = True, 
                    before: str = '', 
                    pageSize: int = 20, 
                    sort: Literal["FIRST_PUBLISHED", "UPDATED", "LAST_PUBLISHED", "CREATED", "CURATED"] = "LAST_PUBLISHED",
                    verified: bool=None) -> SearchResponse:
    """Returns a `SearchResponse` object, or None if no maps could be found.
    :param: after       Only include maps after a certain date (YYYY-MM-DDTHH:MM:SS+00:00)
    :param: automapper  Whether it should include automapped songs.
    :param: before      Only include maps before certain date (YYYY-MM-DDTHH:MM:SS+00:00)
    :param: pageSize    Amount of results to include per page
    :param: sort        Order in which to sort the maps on the page
    :param: verified    Whether or not to filter by verified mapper. True means verified only, and false means unverified only. None means both.
    """
    parameters = {
        "after": after,
        "automapper": automapper,
        "before": before,
        "pageSize": pageSize,
        "sort": sort,
        "verified": verified 
    }
    if after == '': parameters.pop("after")
    if before == '': parameters.pop("before")
    if verified == None: parameters.pop("verified")

    encodedUrl = urlencode(parameters)

    response = _r.get(
        f'{base_url}/maps/latest?{encodedUrl}'
        )

    details = SearchResponse(**response.json())

    return details


def get_maps_by_plays(page: int = 0) -> SearchResponse:
    """Returns a `SearchResponse` object of maps sorted by playcount. BeatSaver API Docs currently say that this is \"Not Currently Tracked.\""""
    response = _r.get(f'{base_url}/maps/plays/{page}')

    details = SearchResponse(**response.json())
    return details

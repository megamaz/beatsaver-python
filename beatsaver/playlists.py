"""All forms of requests involving playlists."""

import requests
from .models.models import *
from .models.exceptions import *
from urllib.parse import urlencode

base_url = "https://beatsaver.com/api"
_r = requests.Session()

def get_latest_playlists(before:str=None, after:str=None, pageSize:int=20, sort:Literal["UPDATED", "SONGS_UPDATED", "CREATED", "CURATED"]="CREATED") -> List[PlaylistFull]:
    """Returns a list of `PlaylistFull`. If no playlists are found, the list will be empty."""

    params = {
        "pageSize": pageSize,
        "sort": sort
    }
    if before is not None:
        params["before"] = before
    if after is not None:
        params["after"] = after
    
    response = _r.get(f'{base_url}/playlists/latest?{urlencode(params)}')

    details = PlaylistSearchResponse(**response.json())
    return details.docs

def get_playlists_by_user(userId:int, page:int=0) -> List[PlaylistFull]:
    """Returns a list of `PlaylistFull` objects containing the playlists created by the user. If no playlists are found, the list will be empty."""

    response = _r.get(f"{base_url}/playlists/user/{userId}/{page}")

    details = PlaylistSearchResponse(**response.json())
    return details.docs

def get_playlists(id:int, page:int=0) -> PlaylistPage:
    """Returns a `PlaylistPage` object containing the requested playlist details. Raises `BeatSaverNotFoundException` if the playlist couldn't be found."""

    response = _r.get(f"{base_url}/playlists/id/{id}/{page}")

    if response.status_code == 404:
        raise BeatSaverNotFoundException(f"Error response: {response.json()['error']}")

    details = PlaylistPage(**response.json())
    return details

def modify_playlist(oauth:PlaylistBatchRequest, id:int) -> ActionResponse:
    """Allows you to modify a playlist. [TODO add details on how to format oauth]. Returns an `ActionResponse` object, or raises `BeatSaverPlaylistModificationFailedException` if an error arises."""

    response = _r.post(f"{base_url}/playlists/{id}/batch", body=oauth.__dict__)
    
    # I actually couldn't get this endpoint to work. It always returned a 404 not found no matter what I did.
    if response.status_code != 200:
        raise BeatSaverUknownException(f"Error response: {response.json()['error']}")
    
    details = ActionResponse(**response.json())
    if not details.success:
        raise BeatSaverPlaylistModificationFailedException(f"Error responses: {details.errors}")
    return ActionResponse(**response.json())
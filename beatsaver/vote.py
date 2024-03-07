"""All form of requests involving voting"""

import requests
from .models.models import *
from .models.exceptions import *

base_url = "https://beatsaver.com/api"
_r = requests.Session()

def get_votes(since:str) -> List[VoteSummary]:
    """Returns a list of `VoteSummary` objects. Raises `BeatSaverArgumentException` if date is not formatted correctly.
    :param: since       A date string (YYYY-MM-DDTHH:MM:SS+00:00)"""
    response = _r.get(f'{base_url}/vote?since={str(since)}')

    if response.status_code == 400: # undocumented
        raise BeatSaverArgumentException(f"Error response: {response.json()['error']}")
    if response.status_code == 404: # docs say this can return a 404 but I couldn't get a 404 to trigger. wtf?
        raise BeatSaverNotFoundException(f"Error response: {response.json()['error']}")
    
    details = [VoteSummary(**x) for x in response.json()]
    return details

def vote_on_map(vote:VoteRequest) -> VoteResponse:
    """Returns a `VoteResponse` object. Raises `BeatSaverOauthFailedException` if the oauth fails."""

    response = _r.post(f"{base_url}/vote", body=({"auth":vote.auth.__dict__}).update(vote.__dict__))
    details = VoteResponse(**response.json())

    if not details.success:
        raise BeatSaverOauthFailedException(f"Error response: {details.error}")
    
    return details
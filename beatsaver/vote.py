"""All form of requests involving voting"""

import requests
from .models.model import *

base_url = "https://beatsaver.com/api"

def get_votes(since:Instant) -> ListOfVoteSummary:
    """Returns a `ListOfVoteSummary` object, or None if no maps are found."""
    r = requests.get(f'{base_url}/vote?since={str(since)}')

    if r.status_code == 404:
        return None
    
    details = ListOfVoteSummary(**r.json())
    return details

def vote_on_map(auth:AuthRequest, vote:VoteRequest) -> VoteResponse:
    """Returns a `VoteResponse` object, or None if the vote failed."""

    r = requests.post(f"{base_url}/vote", body=({"auth":auth.__dict__}).update(vote.__dict__))
    if r.status_code == 404:
        return None
    
    details = VoteResponse(**r.json())
    return details
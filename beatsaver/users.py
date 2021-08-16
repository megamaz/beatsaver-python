"""All form of requests involving users."""

import requests
from .models.model import *

base_url = "https://beatsaver.com/api"

def get_user_info(id:int) -> UserDetail:
    """returns a `UserDetail` object, or None if the user couldn't be found."""

    r = requests.get(f'{base_url}/users/id/{id}')
    if r.status_code == 404:
        return None
    
    details = UserDetail(**r.json())
    return details

def verify_user_token(noReflectionBody:AuthRequest) -> VerifyResponse:
    """returns a `VerifyResponse` object, or None if the user could not be verified."""
    r = requests.post(f'{base_url}/users/verify', body=noReflectionBody.__dict__)

    if r.status_code == 404:
        return None
    
    details = VerifyResponse(**r.json())
    return details
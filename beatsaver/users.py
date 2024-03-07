"""All form of requests involving users."""

import requests
from .models.models import *
from .models.exceptions import *

base_url = "https://beatsaver.com/api"
_r = requests.Session()

def get_user_info(id:int) -> UserDetail:
    """returns a `UserDetail` object containing the details of the requested user. Raises `BeatSaverNotFoundException` if the user couldn't be found."""

    response = _r.get(f'{base_url}/users/id/{id}')
    if response.status_code == 404:
        raise BeatSaverNotFoundException(f"Error response: {response.json()['error']}")
    
    details = UserDetail(**response.json())
    return details

def get_users_info(*ids:int) -> List[UserDetail]:
    """Returns a list of `UserDetail`, one for each ID. If a user is not found, then they will be omitted from the list. If none of the users are found, the list will be empty."""
    users = []
    response = _r.get(f'{base_url}/users/ids/{','.join([str(x) for x in ids])}')

    for u in response.json():
        users.append(UserDetail(**u))
        
    return users

def get_user_info_by_name(name:str) -> UserDetail:
    """returns a `UserDetail` object containing the details of the requested user. Raises `BeatSaverNotFoundException` if no user could be found."""
    response = _r.get(f"{base_url}/users/name/{name}")

    if response.status_code == 400:
        raise BeatSaverArgumentException(f"Error response: {response.json()['error']}")
    
    if response.status_code == 404:
        raise BeatSaverNotFoundException(f"Error response: {response.json()['error']}")
    
    details = UserDetail(**response.json())
    return details
    

def verify_user_token(noReflectionBody:AuthRequest) -> VerifyResponse:
    """returns a `VerifyResponse` object. Raises `BeatSaverVerificationFailedException` if the verification fails."""
    response = _r.post(f'{base_url}/users/verify', body=noReflectionBody.__dict__)
    details = VerifyResponse(**response.json())

    if not details.success:
        raise BeatSaverVerificationFailedException(f"Error response: {details.error}")
    
    return details
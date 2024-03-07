"""All exceptions that can be raised while using the library."""


class BaseBeatSaverException(Exception):
    """The base BeatSaver Exception."""
    # This may look useless, and it is right now- but it might get useful in the future.
    ...

class BeatSaverNotFoundException(BaseBeatSaverException):
    ...

class BeatSaverVerificationFailedException(BaseBeatSaverException):
    ...

class BeatSaverArgumentException(BaseBeatSaverException):
    ...

class BeatSaverOauthFailedException(BaseBeatSaverException):
    ...

class BeatSaverPlaylistModificationFailedException(BaseBeatSaverException):
    ... # super specific because it kinda needs it.

class BeatSaverUknownException(BaseBeatSaverException):
    ... # for when I dont know what the fuck happened
"""All form of requests involving search."""

from typing import Any
import requests
from urllib.parse import urlencode
from .models.models import *
from enum import Enum

base_url = "https://beatsaver.com/api"
_r = requests.Session()


class SearchParams:
    """Class for aiding with Search Parameters."""

    def __init__(self,
                 sortOrder: Literal["Latest", "Relevance", "Rating", "Curated"] = "Relevance",
                 automapper: bool | None = True,
                 chroma: bool = None,
                 cinema: bool = None,
                 mappingExtensions: bool = None,
                 noodle: bool = None,
                 curated: bool = None,
                 ranked: bool = None,
                 verified: bool = None,
                 _from: str = None,
                 _to: str = None,
                 fullSpread: bool = None,
                 minBpm: float = None,
                 minDuration: int = None,
                 minNps: float = None,
                 minRating: float = None,
                 maxBpm: float = None,
                 maxDuration: int = None,
                 maxNps: float = None,
                 maxRating: float = None,
                 page: int = 0,
                 query: str = None,
                 tags: str = None) -> None:
        """Parameters:
            - sortOrder: The order to sort the results in.
            - automapper: Whether or not to include automapper maps. True means both, False means AI only, None means human only.
            - chroma: Whether or not to include Chroma maps.
            - cinema: Whether or not to include Cinema maps.
            - mappingExtensions: whether or not to include Mapping Extensions maps.
            - noodle: Whether or not to include Noodle Extensions maps.
            - curated: Whether or not to include curated maps.
            - ranked: Whether or not to include ranked maps (ScoreSaber).
            - verified: Whether or not to include verified maps (ScoreSaber).
            - _from: The minimum date of the results to search for (YYYY-MM-DDTHH:MM:SS+00:00)
            - _to: The maximum date of the results to search for (YYYY-MM-DDTHH:MM:SS+00:00)
            - fullSpread: Whether or not to filter by maps that have all difficulties.
            - minBpm: The minimum BPM of the results to search for.
            - minDuration: The minimum duration of the results to search for.
            - minNps: The minimum NPS of the results to search for.
            - minRating: The minimum rating of the results to search for.
            - maxBpm: The maximum BPM of the results to search for.
            - maxDuration: The maximum duration of the results to search for.
            - maxNps: The maximum NPS of the results to search for.
            - maxRating: The maximum rating of the results to search for.
            - page: Which page to look at.
            - query: The query.
            - tags: A list of tags to filter by as a string of comma-separated strings."""
        # Sort order can't be None
        self.sortOrder = sortOrder
        # Automapper can be None, but it means something, so the value will effectively always be passed.
        self.automapper = automapper

        # oh boy
        if chroma is not None:
            self.chroma = chroma
        if cinema is not None:
            self.cinema = cinema
        if mappingExtensions is not None:
            self.me = mappingExtensions
        if noodle is not None:
            self.noodle = noodle
        if curated is not None:
            self.curated = curated
        if ranked is not None:
            self.ranked = ranked
        if verified is not None:
            self.verified = verified
        if _from is not None:
            self["from"] = _from
        if _to is not None:
            self["to"] = _to
        if fullSpread is not None:
            self.fullSpread = fullSpread
        if maxBpm is not None:
            self.maxBpm = maxBpm
        if minDuration is not None:
            self.minDuration = minDuration
        if maxDuration is not None:
            self.maxDuration = maxDuration
        if minNps is not None:
            self.minNps = minNps
        if maxNps is not None:
            self.maxNps = maxNps
        if minRating is not None:
            self.minRating = minRating
        if maxRating is not None:
            self.maxRating = maxRating
        if minBpm is not None:
            self.minBpm = minBpm
        if page is not None:
            self.page = page
        if query is not None:
            self.query = query
        if tags is not None:
            self.tags = tags

    def __getattribute__(self, __name: str) -> Any:
        return self.__dict__[__name]

    def __setattr__(self, __name: str, __value: Any) -> None:
        self.__dict__[__name] = __value

    def __iter__(self):
        return iter(self.__dict__.items())


def get_maps_from_search(**params:SearchParams) -> SearchResponse:
    """returns a `SearchResponse` object.
    To facilitate search parameters, you can use the `search.SearchParams` class.
    ```py
    >>> from beatsaver.search import get_maps_from_search, SearchParams
    >>> params = SearchParams() # place all of your parameters here. They all have a default value, so you can also leave this blank.
    >>> get_maps_from_search(**params)
    # here would be the actual result of the function as a `SearchResponse` object
    ```
    """
    if params.get("page"):
        searchParams = f"{params['page']}?"
        params.pop('page')
    else:
        searchParams = "0?"
    
    searchParams += urlencode(params)

    response = _r.get(f'{base_url}/search/text/{searchParams}')

    details = SearchResponse(**response.json())
    return details

def get_playlists_from_search(**params: SearchParams) -> List[PlaylistFull]:
    """Returns a list of `PlaylistFull`. If no playlists are found, the list will be empty.
    To facilitate search parameters, you can use the `search.SearchParams` class.
    ```py
    >>> from beatsaver.search import get_playlists_from_search, SearchParams
    >>> params = SearchParams() # place all of your parameters here. They all have a default value, so you can also leave this blank.
    >>> get_playlists_from_search(**params)
    # here would be the actual result of the function as a list of `PlaylistFull` objects"""
    # it is simpler to return the PlaylistSearchResponse.docs because it's the only property it has.
    if params.get("page"):
        searchParams = f"{params['page']}?"
        params.pop('page')
    else:
        searchParams = "0?"
    
    searchParams += urlencode(params)

    response = _r.get(f"{base_url}/playlists/search/{searchParams}")

    details = PlaylistSearchResponse(**response.json())

    return details.docs
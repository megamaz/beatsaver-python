"""All form of requests involving search."""

import requests
from .models.model import *
from enum import Enum

base_url = "https://beatsaver.com/api"

class SortOrder(Enum):
    Latest = "Latest"
    Relevance = "Relevance"
    Rating = "Rating"

def get_maps_from_search(**params) -> SearchResponse:
    """returns a `SearchResponse` object
    :param: sortOrder       Use from search.SortOrder
    :param: automapper      true=both, false=only AI, None=no AI,
    :param: chroma          Whether to include chroma maps or not
    :param: cinema          Whether to include cinema maps or not
    :param: noodle          Whether to include noodle maps or not
    :param: ranked          Whether to include ranked maps or not
    :param: From            Oldest date to include in search
    :param: to              Youngest date to include in search
    :param: fullSpread      I have no clue
    :param: maxBpm          The maximum BPM of the included maps
    :param: minBpm          The minimum BPM of the inlucded maps
    :param: maxDuration     The maximum duration of the included maps
    :param: minDuration     The minimum duration of the inlucded maps
    :param: maxNps          The maximum notes per second of the included maps
    :param: minNps          The minimum notes per second of the included maps
    :param: maxRating       Maximum rating of included maps
    :param: minRating       Minimum rating of included maps
    :param: page            Which page to do the search on
    :param: q               The search query
    """

    searchParams = f"{params['page']}?"
    params.pop('page')
    for x in params:
        searchParams += f'{x}={params[x]}&'
    searchParams = searchParams[:-1]

    r = requests.get(f'{base_url}/search/text/{searchParams}')

    details = SearchResponse(**r.json())
    return details
    
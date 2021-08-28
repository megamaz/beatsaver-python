from dataclasses import dataclass
from typing import List, Union

NoneType = type(None) # I hate is as much as you do but it makes my life so much simpler

class Undefined: # BECAUSE FOR SOME FUCKING REASON NOT ALL VALUES EXIST
    pass # also js moment

class BeatSaverModel:
    """The base BeatSaver model object."""

    def __getitem__(self, value):
        return getattr(self, value)
    
    def __setitem__(self, index, data):
        return setattr(self, index, data)


        
@dataclass
class Instant(BeatSaverModel):

    def __init__(self, **data):
        for x in data:
            self[x] = data[x] # no models, should be fine

    def __str__(self):
        return self.value

    epochSeconds:int
    nanosecondsOfSecond:int
    value:str

class UserDiffStats(BeatSaverModel):

    def __init__(self, **data):
        for x in data:
            self[x] = data[x]

    easy:int
    expert:int
    expertPlus:int
    hard:int
    normal:int
    total:int

@dataclass
class UserStats(BeatSaverModel):

    def __init__(self, **data):
        for x in data:
            if type(data[x]) == dict:
                continue # skip models
            self[x] = data[x]
        
        self['diffStats'] = UserDiffStats(**data['diffStats'])
        self['firstUpload'] = Instant(**data['firstUpload'])
        self['lastUpload'] = Instant(**data['lastUpload'])

    avgBpm:float
    avgDuration:float
    avgScore:float
    diffStats:UserDiffStats
    firstUpload:Instant
    lastUpload:Instant
    rankedMaps:int
    totalDownvotes:int
    totalMaps:int
    totalUpvotes:int

@dataclass
class UserDetail(BeatSaverModel):

    def __init__(self, **data):
        for x in data:
            if type(data[x]) == dict:
                continue # skip models
            self[x] = data[x]
        if data.get('stats'):
            self['stats'] = UserStats(**data['stats'])
        else:
            self['stats'] = None
        

    avatar:str
    hash:str
    id:int
    name:str
    stats:UserStats # ANOTHER FUCKING VALUE THAT'S INCONSISTENT FFS
    testplay:bool = None # WHY DO YOU NOT ALWAYS EXIST WHAT
        
@dataclass
class MapStats(BeatSaverModel):

    def __init__(self, **data):
        for x in data:
            self[x] = data[x]

    downloads:int
    downvotes:int
    plays:int
    score:float
    upvotes:int

@dataclass
class MapDetailMetadata(BeatSaverModel):

    def __init__(self, **data):
        for x in data:
            self[x] = data[x]

    bpm:float
    duration:int
    levelAuthorName:str
    songAuthorName:str
    songName:str
    songSubName:str

@dataclass
class MapParitySummary(BeatSaverModel):

    def __init__(self, **data):
        for x in data:
            self[x] = data[x]

    errors:int
    resets:int
    warns:int

@dataclass
class MapDifficulty(BeatSaverModel):

    def __init__(self, **data):
        for x in data:
            if type(data[x]) == dict:
                continue
            self[x] = data[x]
        self['paritySummary'] = MapParitySummary(**data['paritySummary'])

    bombs:int
    characteristic:str
    chroma:bool
    cinema:bool
    difficulty:str
    events:int
    length:float
    me:bool
    ne:bool
    njs:float
    notes:int
    nps:float
    obstacles:int
    offset:float
    paritySummary:MapParitySummary
    seconds:float
    stars:float

@dataclass
class MapVersion(BeatSaverModel):

    def __init__(self, **data):
        for x in data:
            if type(data[x]) == dict:
                continue
            self[x] = data[x]
        
        self['diffs'] = [MapDifficulty(**x) for x in data['diffs']]

    coverURL:str
    previewURL:str
    createdAt:Instant
    diffs:List[MapDifficulty]

@dataclass
class MapDetail(BeatSaverModel):

    def __init__(self, **data):
        for x in data:
            if type(data[x]) == dict:
                continue
            self[x] = data[x]
        self['stats'] = MapStats(**data['stats'])
        self['metadata'] = MapDetailMetadata(**data['metadata'])
        if type(data['uploaded']) != str:
            self['uploaded'] = Instant(**data['uploaded']) # GOD FFS
        self['uploader'] = UserDetail(**data['uploader'])

        self['versions'] = [MapVersion(**x) for x in data['versions']]

    automapper:bool
    description:str
    id:str
    metadata:MapDetailMetadata
    name:str
    qualified:bool
    ranked:bool
    stats:MapStats
    uploaded:Union[Instant, str] # WHY IN THE WORLD IS IT MARKED AS INSTANT IN THE DOCS BUT RETURNS A STRING ON SOME MAPS????
    uploader:UserDetail
    versions:List[MapVersion]
    curator:str = None # not all maps have a curator


@dataclass
class MapTestPlay(BeatSaverModel):
    
    def __init__(self, **data):
        for x in data:
            if type(data[x]) == dict:
                continue
            self[x] = data[x]
        self['createdAt'] = Instant(**data['createdAt'])
        self['feedbackAt'] = Instant(**data['feedbackAt'])
        self['user'] = UserDetail(**data['user'])

    createdAt:Instant
    feedback:str
    feedbackAt:Instant
    user:UserDetail
    video:str

@dataclass
class SearchResponse(BeatSaverModel):

    def __init__(self, **data):
        for x in data:
            if type(data[x]) == dict:
                continue
            self[x] = data[x]
        if data.get('docs'): self['docs'] = [MapDetail(**x) for x in data['docs']]
        else: self['docs'] = None

        if data.get('user'): self['user'] = UserDetail(**data['user'])
        else: self['user'] = None
    docs:List[MapDetail]
    redirect:str
    user:UserDetail

@dataclass
class AuthRequest(BeatSaverModel):

    def __init__(self, **data):
        for x in data:
            self[x] = data[x]

    oculusId:str
    proof:str
    steamId:str

@dataclass
class VerifyResponse(BeatSaverModel):

    def __init__(self, **data):
        for x in data:
            self[x] = data[x]

    error:str
    success:bool

@dataclass
class VoteSummary(BeatSaverModel):

    def __init__(self, **data):
        for x in data:
            self[x] = data[x]

    downvotes:int
    hash:str
    key64:str
    mapId:int
    score:float
    upvotes:int

@dataclass
class ListOfVoteSummary(BeatSaverModel):

    def __init__(self, **data):
        self['ListOfVoteSummary'] = [VoteSummary(**x) for x in data['ListOfVoteSummary']]
        
    ListOfVoteSummary:List[VoteSummary]

@dataclass
class VoteRequest(BeatSaverModel):
    def __init__(self, **data):
        for x in data:
            if type(data[x]) == dict:
                continue
            self[x] = data[x]
        self['auth'] = AuthRequest(**data['auth'])
    auth:AuthRequest
    direction:bool
    hash:str

@dataclass
class VoteResponse(BeatSaverModel):

    def __init__(self, **data):
        for x in data:
            self[x] = data[x]

    error:str
    success:bool

from dataclasses import dataclass
from typing import Any, List, Union, Literal


class BeatSaverModel:
    """The base BeatSaver model object."""

    def __init__(self, **data):
        self.__dict__ = data

    def __getattr__(self, __name: str) -> Any: # ensures that properties that are unset don't raise an error for being unset.
        return

@dataclass
class Response:
    error: str
    success: bool


@dataclass
class UserFollowData(BeatSaverModel):
    curation: bool
    followers: int
    following: bool
    follows: int
    upload: bool


@dataclass
class UserDiffStats(BeatSaverModel):
    easy: int
    expert: int
    expertPlus: int
    hard: int
    normal: int
    total: int


@dataclass
class UserStats(BeatSaverModel):

    def __init__(self, **data):
        self.__dict__ = data

        if data.get("diffStats"):
            self.diffStats = UserDiffStats(**data["diffStats"])

    avgBpm: float
    avgDuration: float
    avgScore: float
    diffStats: UserDiffStats
    firstUpload: str
    lastUpload: str
    rankedMaps: int
    totalDownvotes: int
    totalMaps: int
    totalUpvotes: int


@dataclass
class UserDetail(BeatSaverModel):

    def __init__(self, **data):
        self.__dict__ = data

        if data.get("followData"):
            self.followData = UserFollowData(**data["followData"])
        if data.get("stats"):
            self.stats = UserStats(**data["stats"])

    admin: bool
    avatar: str
    curator: bool
    curatorTab: bool
    description: str
    email: str
    followData: UserFollowData
    hash: str
    id: int
    name: str
    patreon: Literal["None", "Supporter", "SupporterPlus"]
    playlistUrl: str
    seniorCurator: bool
    stats: UserStats
    suspendedAt: str
    testplay: bool
    type: Literal["DISCORD", "SIMPLE", "DUAL"]
    uniqueSet: bool
    uploadLimit: int
    verifiedMapper: bool


@dataclass
class MapDetailMetadata(BeatSaverModel):
    bpm: float
    duration: int
    levelAuthorName: str
    songAuthorName: str
    songName: str
    songSubName: str


@dataclass
class MapStats(BeatSaverModel):
    downloads: int
    downvotes: int
    plays: int
    score: float
    upvotes: int
    scoreOneDP: float = None
    # For some reason, this value can be missing even though "Pending" exists
    sentiment: Literal["PENDING", "VERY_NEGATIVE", "MOSTLY_NEGATIVE",
                       "MIXED", "MOSTLY_POSITIVE", "VERY_POSITIVE"] = None
    reviews: int = None


@dataclass
class MapParitySummary(BeatSaverModel):
    errors: int
    resets: int
    warns: int


@dataclass
class MapTestplay(BeatSaverModel):

    def __init__(self, **data):
        self.__dict__ = data

        if data.get("user"):
            self.user = UserDetail(**data["user"])

    createdAt: str
    feedback: str
    feedbackAt: str
    user: UserDetail
    video: str


@dataclass
class MapDifficulty(BeatSaverModel):

    def __init__(self, **data):
        self.__dict__ = data

        if data.get("paritySummary"):
            self.paritySummary = MapParitySummary(**data["paritySummary"])

    bombs: int
    characteristic: Literal["Standard", "OneSaber", "NoArrows",
                            "90Degree", "360Degree", "Lightshow", "Lawless", "Legacy"]
    chroma: bool
    cinema: bool
    difficulty: Literal["Easy", "Normal", "Hard", "Expert", "ExpertPlus"]
    events: int
    label: str
    length: float
    maxScore: int
    me: bool
    ne: bool
    njs: float
    notes: int
    nps: float
    obstacles: int
    offset: float
    paritySummary: MapParitySummary
    seconds: float
    stars: float


@dataclass
class MapVersion(BeatSaverModel):

    def __init__(self, **data):
        self.__dict__ = data

        if data.get("diffs"):
            self.diffs = [MapDifficulty(**x) for x in data["diffs"]]
        if data.get("testplays"):
            self.testplays = [MapTestplay(**x) for x in data["testplays"]]

    coverURL: str
    createdAt: str
    diffs: List[MapDifficulty]
    downloadURL: str
    feedback: str
    hash: str
    key: str
    previewURL: str
    sageScore: int
    scheduledAt: str
    state: Literal["Uploaded", "Testplay",
                   "Published", "Feedback", "Scheduled"]
    testplayAt: str
    testplays: List[MapTestplay]


@dataclass
class MapDetail(BeatSaverModel):

    def __init__(self, **data):
        self.__dict__ = data

        if data.get("collaborators"):
            self.collaborators = [UserDetail(**x)
                                  for x in data["collaborators"]]
        if data.get("curator"):
            self.curator = UserDetail(**data["curator"])
        if data.get("metadata"):
            self.metadata = MapDetailMetadata(**data["metadata"])
        if data.get("stats"):
            self.stats = MapStats(**data["stats"])
        if data.get("uploader"):
            self.uploader = UserDetail(**data["uploader"])
        if data.get("versions"):
            self.versions = [MapVersion(**x) for x in data["versions"]]

    automapper: bool
    bookmarked: bool
    collaborators: List[UserDetail]
    createdAt: str
    curatedAt: str
    curator: UserDetail
    declaredAi: Literal["Admin", "Uploader", "SageScore", "None"]
    deletedAt: str
    description: str
    id: str
    lastPublishedAt: str
    metadata: MapDetailMetadata
    name: str
    qualified: bool
    ranked: bool
    stats: MapStats
    tags: List[Literal['None', 'Tech', 'DanceStyle', 'Speed', 'Balanced', 'Challenge', 'Accuracy', 'Fitness', 'Swing', 'Nightcore', 'Folk', 'Family', 'Ambient', 'Funk', 'Jazz', 'Classical', 'Soul', 'Speedcore', 'Punk', 'RB', 'Holiday',
                       'Vocaloid', 'JRock', 'Trance', 'DrumBass', 'Comedy', 'Instrumental', 'Hardcore', 'KPop', 'Indie', 'Techno', 'House', 'Game', 'Film', 'Alt', 'Dubstep', 'Metal', 'Anime', 'HipHop', 'JPop', 'Dance', 'Rock', 'Pop', 'Electronic']]
    updatedAt: str
    uploaded: str
    uploader: UserDetail
    versions: List[MapVersion]


@dataclass
class SearchResponse(BeatSaverModel):

    def __init__(self, **data):
        self.__dict__ = data

        if data.get("docs"):
            self.docs = [MapDetail(**x) for x in data["docs"]]

    docs: List[MapDetail]
    redirect: str


@dataclass
class AuthRequest(BeatSaverModel):
    oculusId: str
    proof: str
    steamId: str


@dataclass
class VerifyResponse(BeatSaverModel, Response):
    ...


@dataclass
class VoteSummary(BeatSaverModel):
    downvotes: int
    hash: str
    key64: str
    mapId: int
    score: float
    upvotes: int


@dataclass
class ListOfVoteSummary(BeatSaverModel):  # Why is this a thing?
    self: List[VoteSummary]


@dataclass
class VoteRequest(BeatSaverModel):

    def __init__(self, **data):
        self.__dict__ = data

        if data.get("auth"):
            self.auth = AuthRequest(**data["auth"])

    auth: AuthRequest
    direction: bool
    hash: str


@dataclass
class VoteResponse(BeatSaverModel, Response):
    ...


@dataclass
class IPlaylistConfig(BeatSaverModel):
    ...  # the docs do not have any data on IPlaylistConfig


@dataclass
class PlaylistStats(BeatSaverModel):
    avgScore: float
    downVotes: int
    mapperCount: int
    maxNps: float
    maxNpsTwoDP: float
    minNps: float
    minNpsTwoDP: float
    scoreOneDP: float
    totalDuration: int
    totalMaps: int
    upVotes: int


@dataclass
class PlaylistFull(BeatSaverModel):

    def __init__(self, **data):
        self.__dict__ = data

        if data.get("config"):
            self.config = IPlaylistConfig(**data["config"])
        if data.get("curator"):
            self.curator = UserDetail(**data["curator"])
        if data.get("owner"):
            self.owner = UserDetail(**data["owner"])
        if data.get("stats"):
            self.stats = PlaylistStats(**data["stats"])

    config: IPlaylistConfig
    createdAt: str
    curatedAt: str
    curator: UserDetail
    deletedAt: str
    description: str
    downloadURL: str
    name: str
    owner: UserDetail
    playlistId: int
    playlistImage: str
    playlistImage512: str
    songsChangedAt: str
    stats: PlaylistStats
    type: Literal["Private", "Public", "System", "Search"]
    updatedAt: str


@dataclass
# this feels useless. Just return a List[PlaylistFull].
class PlaylistSearchResponse(BeatSaverModel):

    def __init__(self, **data):
        self.__dict__ = data

        if data.get("docs"):
            self.docs = [PlaylistFull(**x) for x in data["docs"]]

    docs: List[PlaylistFull]


@dataclass
class MapDetailWithOrder(BeatSaverModel):

    def __init__(self, **data):
        self.__dict__ = data

        if data.get("map"):
            self.map = MapDetail(**data["map"])

    map: MapDetail
    order: float


@dataclass
class PlaylistPage(BeatSaverModel):

    def __init__(self, **data):
        self.__dict__ = data

        if data.get("maps"):
            self.maps = [MapDetailWithOrder(**x) for x in data["maps"]]
        if data.get("playlist"):
            self.playlist = PlaylistFull(**data["playlist"])

    maps: List[MapDetailWithOrder]
    playlist: PlaylistFull


@dataclass
class PlaylistBatchRequest(BeatSaverModel):
    hashes: List[str]
    ignoreUnknown: bool
    inPlaylist: bool
    keys: List[str]


@dataclass
class ActionResponse(BeatSaverModel, Response):
    errors: List[str]

from enum import Enum, auto


class Status(Enum):
    """Possible statuses for response."""

    MOVIE_NOT_FOUNT = auto()
    RATE_NOT_FOUND = auto()

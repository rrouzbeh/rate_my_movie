
from rate_my_movie.enums import Status


COLORS = {
    Status.MOVIE_NOT_FOUNT: "red",
    Status.RATE_NOT_FOUND: "blue"
}

MSG = {
    Status.MOVIE_NOT_FOUNT: "Movie not found!",
    Status.RATE_NOT_FOUND: "Rate not found!",
}

DEFAULT_COLOR = "green"

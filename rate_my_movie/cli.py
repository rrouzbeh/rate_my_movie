
from rate_my_movie.omdbapi import RottenTomato, GetMovieInfo
from rate_my_movie.config.config import settings
from rate_my_movie.utils import console_output, handle_args


def main():
    title = handle_args()
    movie = GetMovieInfo(api_key=settings.get('api_key'))
    obj = movie.get(title=title)
    movie_info = RottenTomato(**obj)
    console_output(movie_info.rate(), title)


if __name__ == "__main__":
    main()

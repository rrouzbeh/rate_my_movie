from unittest.mock import Mock

import pytest

from rate_my_movie.omdbapi import GetMovieInfo, RottenTomato, MovieInfo
from rate_my_movie.enums import Status

DATA_OK = {
    "Title": "Inception",
    "Ratings": [
        {"Source": "Internet Movie Database", "Value": "8.8/10"},
        {"Source": "Rotten Tomatoes", "Value": "87%"},
        {"Source": "Metacritic", "Value": "74/100"}
    ],
    "Response": "True"
}

DATA_RATE_NOTE_FOUND = {
    "Title": "Inception",
    "Ratings": [
        {"Source": "Internet Movie Database", "Value": "8.8/10"},
        {"Source": "Metacritic", "Value": "74/100"}
    ],
    "Response": "True"
}

DATA_MOVIE_NOT_FOUND = {"Response": "False", "Error": "Movie not found!"}


@pytest.fixture
def get_movie_ok(mocker):
    movie = GetMovieInfo(api_key='xxxxx')
    resp_mock = Mock()
    resp_mock.json.return_value = DATA_OK
    get_mock = mocker.patch('rate_my_movie.omdbapi.requests.get')
    get_mock.return_value = resp_mock
    return movie


@pytest.fixture
def get_movie_rate_not_found(mocker):
    movie = GetMovieInfo(api_key='xxxxx')
    resp_mock = Mock()
    resp_mock.json.return_value = DATA_RATE_NOTE_FOUND
    get_mock = mocker.patch('rate_my_movie.omdbapi.requests.get')
    get_mock.return_value = resp_mock
    return movie


@pytest.fixture
def get_movie_not_found(mocker):
    movie = GetMovieInfo(api_key='xxxxx')
    resp_mock = Mock()
    resp_mock.json.return_value = DATA_MOVIE_NOT_FOUND
    get_mock = mocker.patch('rate_my_movie.omdbapi.requests.get')
    get_mock.return_value = resp_mock
    return movie


def test_get_movie_data(get_movie_ok):
    """Test get correct data"""
    movie = get_movie_ok.get(title="Inception")

    assert movie == DATA_OK


def test_rotten_tomato_rate_usecase(get_movie_ok):
    """Test rotten_tomato_rate usecase"""

    data = get_movie_ok.get(title="Inception")
    movie_info = RottenTomato(**data)

    assert movie_info.rate() == {"Rotten Tomatoes": "87%"}


def test_rotten_tomato_rate_not_found(get_movie_rate_not_found):
    """Test rotten_tomato_rate whenever rate not exist"""
    data = get_movie_rate_not_found.get(title="Inception")

    movie_info = RottenTomato(**data)

    assert movie_info.rate() == {"Rotten Tomatoes": Status.RATE_NOT_FOUND}


def test_rotten_tomato_movie_not_found(get_movie_not_found):
    """Test rotten_tomato_rate whenever movie not found"""
    data = get_movie_not_found.get(title="Inception")

    movie_info = RottenTomato(**data)

    assert movie_info.rate() == {"Error": Status.MOVIE_NOT_FOUNT}

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional

from pydantic import BaseModel
import requests

from rate_my_movie.enums import Status


class Ratings(BaseModel):

    Source: str
    Value: str


class GetMovieInfo(BaseModel):

    url: str = "http://www.omdbapi.com"
    api_key: str
    movie_info: Dict = {}

    def get(self, title: str) -> Dict:
        payload: Dict = {'t': title, 'apikey': self.api_key}
        self.movie_info = requests.get(url=self.url, params=payload).json()
        return self.movie_info


class MovieInfo(BaseModel, ABC):
    """Basic representation of the movie information"""

    Title: Optional[str]
    Ratings: Optional[List[Ratings]]
    Response: str
    rates: dict

    def __init__(self, **data: Any):
        super().__init__(**data)
        if self.Ratings:
            for rate in self.Ratings:
                self.rates[rate.Source] = rate.Value

    @abstractmethod
    def rate(self) -> Dict:
        """Method to call for getting rate of the movie"""
        pass


class RottenTomato(MovieInfo):

    rates: Dict = {}

    def rate(self):
        if self.Response == "True":
            rate: dict = {}
            rate["Rotten Tomatoes"] = self.rates.get(
                "Rotten Tomatoes", Status.RATE_NOT_FOUND)
            return rate
        else:
            return {"Error": Status.MOVIE_NOT_FOUNT}

# Rate My Movie

![ci workflow](https://github.com/rrouzbeh/rate_my_movie/actions/workflows/main.yml/badge.svg)

A simple tool to check out the rotten tomatoes score.

# Installation

clone the git repository to your machine

```
git clone https://github.com/rrouzbeh/rate_my_movie.git
cd rate_my_movie
```

## Local Installation

For local installation, please follow the bellow instructions

```
make init
make install
make test
```

## Docker Installation

You may use either the prebuilt `rrouzbeh/rate-my-movie` docker image or build your own docker image.

### Build docker image locally

```
make docker
```

# Usage

## Local Machine

In order to add an OMDBAPI key to rate-my-movie, there are two methods:

- Environment variable:

```
export MOVIE_API_KEY="<APIKEY>"
```

- Dynaconf secretfile:
  Add `api_key: <APIKEY>` to `rate_my_movie/config/.secrets.yaml`.

```
rate-my-movie TITLE
```

## Docker

```
docker run --rm -t -e MOVIE_API_KEY="<APIKEY>" rate-my-movie TITLE
```

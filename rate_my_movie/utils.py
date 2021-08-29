import sys

from rich.console import Console

from rate_my_movie.enums import Status


console = Console()

COLORS = {
    Status.MOVIE_NOT_FOUNT: "red",
    Status.RATE_NOT_FOUND: "blue"
}

MSG = {
    Status.MOVIE_NOT_FOUNT: "Movie not found!",
    Status.RATE_NOT_FOUND: "Rate not found!",
}

DEFAULT_COLOR = "green"


def handle_args() -> str:
    if len(sys.argv) < 2:
        console.print("Usage: rate-my-movie TITLE \n")
        console.print("You must enter the movie's title \n",
                      style="bold red")
        exit(0)
    return ' '.join(sys.argv[1:])


def console_output(data: dict, title: str) -> None:
    console.print(
        f"\n[bold blue]Movie[/bold blue]: [magenta]{ title.capitalize() }[/magenta]")
    for k, v in data.items():
        color = COLORS.get(v, DEFAULT_COLOR)
        msg = MSG.get(v, v)
        console.print(
            f"\n[bold { color }]{k}[/bold {color}]: [cyan]{msg}[/cyan] \n")

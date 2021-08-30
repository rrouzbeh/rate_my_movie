from setuptools import setup
import io
import os


def read(*names, **kwargs):
    """Read a file."""
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


setup(
    name="rate-my-movie",
    version=read("rate_my_movie", "VERSION"),
    packages=["rate_my_movie", "rate_my_movie.config"],
    include_package_data=True,
    entry_points="""
        [console_scripts]
        rate-my-movie=rate_my_movie.cli:main
    """,
)

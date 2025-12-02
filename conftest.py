import pytest
import logging
import pathlib


@pytest.fixture
def api_url():
    return "https://jsonplaceholder.typicode.com/"




path_dir = pathlib.Path("logs")
path_dir.mkdir(exist_ok=True)


logging.basicConfig(
    filename= path_dir/ "historial.log"
)








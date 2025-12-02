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

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "<h2>MISION IMPOSIBLE CUMPLIDA</h2>",
        '<div style="background:gold">¡Pruebas terminadas!</div>'
    ])

path_dir = pathlib.Path("logs")
path_dir.mkdir(exist_ok=True)


@pytest.fixture(scope='session', autouse=True)
def setup_logging():
    logging.basicConfig(
        filename=path_dir / "historial.log",
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(name)s [%(message)s]',
        datefmt='%H:%M:%S'
    )
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    yield

logger = logging.getLogger()
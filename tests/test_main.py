from http import HTTPStatus

from fastapi.testclient import TestClient
from structlog.testing import capture_logs

from app.main import app

client = TestClient(app)


def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == HTTPStatus.OK
    assert response.text == ""


def test_root():
    # Example of testing logging using a context manager
    with capture_logs() as cap_logs:
        response = client.get("/?token=jessica")
        assert {"event": "In root path", "log_level": "info"} in cap_logs
        assert response.status_code == HTTPStatus.OK
        assert response.json() == {"message": "Hello Bigger Applications!"}

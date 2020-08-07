from datetime import datetime
from os.path import join, exists, getmtime
from fastapi.testclient import TestClient

try:
    from fastapi_server.app.main import app
    from fastapi_server.app.settings import FILES_DIR, ROOT_PATH
except ModuleNotFoundError:
    from main import app
    from settings import FILES_DIR, ROOT_PATH


client = TestClient(app)


def test_upload_file():
    response = client.post(
        "/file/upload/",
        files={"file": ("requirements.txt", open(join(ROOT_PATH, 'requirements.txt'), "rb"))}
    )
    assert response.status_code == 200
    assert exists(join(FILES_DIR, 'requirements.txt'))


def test_status():
    response = client.get(
        "/file/status/",
        json={"full_name": 'requirements.txt'}
    )
    assert response.status_code == 200
    assert response.json().get('full_name') == "requirements.txt"


def test_download():
    response = client.get(
        "/file/download/requirements.txt",
    )
    assert response.status_code == 200
    assert 'aiofiles', 'certifi' in response.text


def test_delete():
    response = client.delete(
        "/file/delete/requirements.txt",
    )
    assert response.status_code == 200
    assert not exists(join(FILES_DIR, 'requirements.txt'))

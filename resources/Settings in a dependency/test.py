from fastapi.testclient import TestClient
from .Setting import Setting
from .main import app, get_settings

client = TestClient(app)

def get_settings_override():
    return Settings(PROJECT_NAME="TEST_PROJECT_NAME")

app.dependency_overrides[get_settings] = get_settings_override

def test_app():
    response = client.get("/info")
    data = response.json()
    assert data == {
        "PROJECT_NAME": "TEST_PROJECT_NAME"
    }
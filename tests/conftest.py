from typing import AsyncGenerator, Generator
import pytest
from fastapi import FastAPI
# from fastapi.testclient import TestClient
from starlette.testclient import TestClient
from httpx import AsyncClient
from app.main import app
from app.configs.database import connect_to_database, close_database_connection

'''
# @pytest.fixture(scope="module")
# def test_app():
#     # Perform setup tasks before testing (e.g., connect to test database)
#     connect_to_database()
#     yield TestClient(app)  # Provide the TestClient instance
#     # Perform cleanup tasks after testing (e.g., close test database connection)
#     close_database_connection()
'''

# Provide the test client to all test functions that need it
@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as client:
        yield client

# Initialize database connection for testing
@pytest.fixture(autouse=True)
async def db() -> AsyncGenerator:
    connect_to_database()
    yield
    close_database_connection()

@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url=client.base_url) as ac:
        yield ac








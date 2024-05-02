from typing import AsyncGenerator, Generator
import pytest
import json as json
import urllib.parse
from app.main import app
from app.configs.database import connect_to_database, close_database_connection

def test_check_health_success(client, db):
    try:
        test_request_endpoint = f"/v1/applications/check-health"
        response = client.get(test_request_endpoint)
        assert response.status_code == 200
    except Exception as e:
        raise e # Re-raise the exception to fail the test
    
# def test_login_success(client, db):
#     try:
#         test_request_endpoint = f"/v1/login"
#         test_request_payload = {"username": "kasunvmail@gmail.com", "password": "password"}
#         test_response_payload = {}
#         # response = client.post(test_request_endpoint, data=json.dumps(test_request_payload))
#         response = client.post(test_request_endpoint, data=test_request_payload)
#         assert response.status_code == 200
#         # assert "access_token" in response.json()
#     except Exception as e:
#         raise e # Re-raise the exception to fail the test
    
# def test_test_token_failure(client, db):
#     try:
#         test_request_endpoint = f"/v1/test-token"
#         access_token = "invalid_access_token"
#         headers = {"Authorization": f"Bearer {access_token}"}
#         response = client.post(test_request_endpoint, headers=headers)
#         assert response.status_code == 401
#     except Exception as e:
#         raise e # Re-raise the exception to fail the test


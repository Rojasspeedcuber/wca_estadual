import logging
from unittest.mock import Mock

import api


def test_invalid_user_token_is_not_logged(monkeypatch, caplog):
    monkeypatch.setattr(api, "get_wca_id_from_token", lambda token: "another-user")
    client = api.app.test_client()
    with caplog.at_level(logging.WARNING):
        response = client.post("/user/2022SOUZ13", json={"state": "PE", "access_token": "sensitive-token"})
    assert response.status_code == 200
    assert response.json is not None
    assert response.json["code"] == api.USER_NOT_CREATED
    assert "sensitive-token" not in caplog.text


def test_other_origin_cannot_use_cors():
    client = api.app.test_client()
    response = client.options("/ranking", headers={"Origin": "https://other.example", "Access-Control-Request-Method": "GET"})
    assert "Access-Control-Allow-Origin" not in response.headers

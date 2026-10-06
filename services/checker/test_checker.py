from unittest.mock import MagicMock, patch

import requests

from checker import check_url


def fake_response(status_code):
    response = MagicMock()
    response.status_code = status_code
    return response


@patch("checker.requests.get")
def test_healthy_url_is_up(mock_get):
    mock_get.return_value = fake_response(200)
    result = check_url("https://example.com")
    assert result["is_up"] is True
    assert result["status_code"] == 200
    assert result["error"] is None
    assert result["latency_ms"] is not None


@patch("checker.requests.get")
def test_server_error_is_down(mock_get):
    mock_get.return_value = fake_response(500)
    result = check_url("https://example.com")
    assert result["is_up"] is False
    assert result["status_code"] == 500


@patch("checker.requests.get")
def test_timeout_is_down(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout
    result = check_url("https://example.com")
    assert result["is_up"] is False
    assert result["error"] == "timeout"
    assert result["status_code"] is None


@patch("checker.requests.get")
def test_connection_error_is_down(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError
    result = check_url("https://example.com")
    assert result["is_up"] is False
    assert result["error"] == "ConnectionError"
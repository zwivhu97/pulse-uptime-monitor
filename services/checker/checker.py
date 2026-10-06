import time
from datetime import datetime, timezone

import requests

DEFAULT_TIMEOUT = 5  # seconds


def check_url(url, timeout=DEFAULT_TIMEOUT):
    """Check one URL and return a result dictionary. Never raises."""
    checked_at = datetime.now(timezone.utc).isoformat()
    start = time.perf_counter()

    try:
        response = requests.get(url, timeout=timeout)
        latency_ms = round((time.perf_counter() - start) * 1000, 1)
        return {
            "url": url,
            "status_code": response.status_code,
            "latency_ms": latency_ms,
            "is_up": response.status_code < 500,
            "error": None,
            "checked_at": checked_at,
        }
    except requests.exceptions.Timeout:
        error = "timeout"
    except requests.exceptions.RequestException as exc:
        error = type(exc).__name__

    # Reached only when the request failed outright
    return {
        "url": url,
        "status_code": None,
        "latency_ms": None,
        "is_up": False,
        "error": error,
        "checked_at": checked_at,
    }
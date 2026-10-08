from storage import connect, recent_results, save_result


def make_result(url="https://example.com", is_up=True):
    return {
        "url": url,
        "status_code": 200 if is_up else None,
        "latency_ms": 120.0 if is_up else None,
        "is_up": is_up,
        "error": None if is_up else "timeout",
        "checked_at": "2026-10-07T10:00:00+00:00",
    }


def test_save_and_read_back():
    conn = connect(":memory:")
    save_result(conn, make_result())
    rows = recent_results(conn, "https://example.com")
    assert len(rows) == 1
    assert rows[0]["url"] == "https://example.com"
    assert rows[0]["is_up"] == 1


def test_recent_results_are_newest_first_and_limited():
    conn = connect(":memory:")
    save_result(conn, make_result(is_up=True))
    save_result(conn, make_result(is_up=False))
    save_result(conn, make_result(is_up=False))
    rows = recent_results(conn, "https://example.com", limit=2)
    assert len(rows) == 2
    assert [r["is_up"] for r in rows] == [0, 0]


def test_results_are_kept_separate_per_url():
    conn = connect(":memory:")
    save_result(conn, make_result(url="https://a.example"))
    save_result(conn, make_result(url="https://b.example"))
    assert len(recent_results(conn, "https://a.example")) == 1
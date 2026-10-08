import sqlite3
from pathlib import Path

DEFAULT_DB = Path(__file__).with_name("pulse.db")


def connect(db_path=DEFAULT_DB):
    """Open the database and make sure the checks table exists."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS checks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            status_code INTEGER,
            latency_ms REAL,
            is_up INTEGER NOT NULL,
            error TEXT,
            checked_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    return conn


def save_result(conn, result):
    conn.execute(
        "INSERT INTO checks (url, status_code, latency_ms, is_up, error, checked_at) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (
            result["url"],
            result["status_code"],
            result["latency_ms"],
            int(result["is_up"]),
            result["error"],
            result["checked_at"],
        ),
    )
    conn.commit()


def recent_results(conn, url, limit=3):
    """Newest first."""
    rows = conn.execute(
        "SELECT * FROM checks WHERE url = ? ORDER BY id DESC LIMIT ?",
        (url, limit),
    ).fetchall()
    return [dict(row) for row in rows]
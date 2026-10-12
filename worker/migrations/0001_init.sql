-- Migration number: 0001 	 2026-10-12T20:51:50.822Z
CREATE TABLE checks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  url TEXT NOT NULL,
  status_code INTEGER,
  latency_ms INTEGER,
  is_up INTEGER NOT NULL,
  error TEXT,
  checked_at TEXT NOT NULL
);

CREATE INDEX idx_checks_url_id ON checks (url, id);
-- Migration number: 0002 	 2026-10-13T19:43:38.015Z
CREATE INDEX IF NOT EXISTS idx_checks_url_id ON checks (url, id);
import type { CheckResult } from "./checker";

export interface StoredCheck {
	is_up: number;
	status_code: number | null;
	latency_ms: number | null;
	error: string | null;
	checked_at: string;
}

export async function saveResults(db: D1Database, results: CheckResult[]): Promise<void> {
	const stmt = db.prepare(
		"INSERT INTO checks (url, status_code, latency_ms, is_up, error, checked_at) VALUES (?, ?, ?, ?, ?, ?)",
	);
	await db.batch(
		results.map((r) =>
			stmt.bind(r.url, r.status_code, r.latency_ms, r.is_up ? 1 : 0, r.error, r.checked_at),
		),
	);
}

/** Newest first. */
export async function recentChecks(db: D1Database, url: string, limit: number): Promise<StoredCheck[]> {
	const { results } = await db
		.prepare(
			"SELECT is_up, status_code, latency_ms, error, checked_at FROM checks WHERE url = ? ORDER BY id DESC LIMIT ?",
		)
		.bind(url, limit)
		.all<StoredCheck>();
	return results;
}
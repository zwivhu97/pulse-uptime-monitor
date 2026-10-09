import { afterEach, expect, it, vi } from "vitest";
import { checkUrl } from "../src/checker";

afterEach(() => {
	vi.restoreAllMocks();
});

it("treats a 200 response as up", async () => {
	vi.spyOn(globalThis, "fetch").mockResolvedValue(new Response("ok", { status: 200 }));
	const r = await checkUrl("https://example.com");
	expect(r.is_up).toBe(true);
	expect(r.status_code).toBe(200);
	expect(r.error).toBeNull();
	expect(r.latency_ms).not.toBeNull();
});

it("treats a 500 response as down", async () => {
	vi.spyOn(globalThis, "fetch").mockResolvedValue(new Response("boom", { status: 500 }));
	const r = await checkUrl("https://example.com");
	expect(r.is_up).toBe(false);
	expect(r.status_code).toBe(500);
});

it("treats a timeout as down", async () => {
	const err = new Error("timed out");
	err.name = "TimeoutError";
	vi.spyOn(globalThis, "fetch").mockRejectedValue(err);
	const r = await checkUrl("https://example.com");
	expect(r.is_up).toBe(false);
	expect(r.error).toBe("timeout");
	expect(r.status_code).toBeNull();
});

it("treats a connection failure as down", async () => {
	vi.spyOn(globalThis, "fetch").mockRejectedValue(new TypeError("fetch failed"));
	const r = await checkUrl("https://example.com");
	expect(r.is_up).toBe(false);
	expect(r.error).toBe("TypeError");
});
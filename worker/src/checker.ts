export interface CheckResult {
  url: string;
  status_code: number | null;
  latency_ms: number | null;
  is_up: boolean;
  error: string | null;
  checked_at: string;
}

const DEFAULT_TIMEOUT_MS = 5000;

export async function checkUrl(
  url: string,
  timeoutMs: number = DEFAULT_TIMEOUT_MS,
): Promise<CheckResult> {
  const checkedAt = new Date().toISOString();
  const start = Date.now();

  try {
    const response = await fetch(url, { signal: AbortSignal.timeout(timeoutMs) });
    const latencyMs = Date.now() - start;
    await response.body?.cancel(); // we only need the status, not the body
    return {
      url,
      status_code: response.status,
      latency_ms: latencyMs,
      is_up: response.status < 500,
      error: null,
      checked_at: checkedAt,
    };
  } catch (err) {
    let error = "unknown";
    if (err instanceof Error) {
      error = err.name === "TimeoutError" ? "timeout" : err.name;
    }
    return {
      url,
      status_code: null,
      latency_ms: null,
      is_up: false,
      error,
      checked_at: checkedAt,
    };
  }
}
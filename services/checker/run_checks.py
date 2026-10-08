import json
from pathlib import Path

from checker import check_url
from detector import is_outage  # NEW
from storage import connect, recent_results, save_result  # NEW

FAILURES_NEEDED = 3  # NEW


def main():
    targets_file = Path(__file__).with_name("targets.json")
    targets = json.loads(targets_file.read_text(encoding="utf-8-sig"))
    conn = connect()  # NEW

    print(f"{'URL':<35} {'STATUS':<8} {'MS':<9} {'UP':<5} {'STATE':<8} ERROR")  # CHANGED
    for url in targets:
        r = check_url(url)
        save_result(conn, r)  # NEW
        recent = recent_results(conn, url, FAILURES_NEEDED)  # NEW
        state = "OUTAGE" if is_outage(recent, FAILURES_NEEDED) else "ok"  # NEW
        status = r["status_code"] if r["status_code"] is not None else "-"
        latency = r["latency_ms"] if r["latency_ms"] is not None else "-"
        print(f"{r['url']:<35} {status!s:<8} {latency!s:<9} {r['is_up']!s:<5} {state:<8} {r['error'] or ''}")  # CHANGED
    conn.close()  # NEW


if __name__ == "__main__":
    main()
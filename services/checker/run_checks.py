import json
from pathlib import Path

from checker import check_url


def main():
    targets_file = Path(__file__).with_name("targets.json")
    targets = json.loads(targets_file.read_text())

    print(f"{'URL':<35} {'STATUS':<8} {'MS':<9} {'UP':<5} ERROR")
    for url in targets:
        r = check_url(url)
        status = r["status_code"] if r["status_code"] is not None else "-"
        latency = r["latency_ms"] if r["latency_ms"] is not None else "-"
        print(f"{r['url']:<35} {status!s:<8} {latency!s:<9} {r['is_up']!s:<5} {r['error'] or ''}")


if __name__ == "__main__":
    main()
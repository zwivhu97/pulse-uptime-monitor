def is_outage(recent, failures_needed=3):
    """True only when we have enough history and every recent check failed.

    `recent` is newest first, as returned by storage.recent_results.
    """
    if len(recent) < failures_needed:
        return False
    return all(not r["is_up"] for r in recent[:failures_needed])

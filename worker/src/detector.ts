export function isOutage(recent: { is_up: number }[], failuresNeeded = 3): boolean {
	if (recent.length < failuresNeeded) {
		return false;
	}
	return recent.slice(0, failuresNeeded).every((r) => r.is_up === 0);
}
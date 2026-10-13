import { checkUrl } from "./checker";
import { isOutage } from "./detector";
import { recentChecks, saveResults } from "./storage";
import { TARGETS } from "./targets";

const FAILURES_NEEDED = 3;

export default {
	async fetch(request: Request, env: Env): Promise<Response> {
		const url = new URL(request.url);

		if (url.pathname === "/status") {
			const targets = await Promise.all(
				TARGETS.map(async (target) => {
					const recent = await recentChecks(env.DB, target, FAILURES_NEEDED);
					return {
						url: target,
						state: isOutage(recent, FAILURES_NEEDED) ? "outage" : "ok",
						last_check: recent[0] ?? null,
					};
				}),
			);
			return Response.json(targets);
		}

		return new Response("Pulse is running. Try /status", { status: 200 });
	},

	async scheduled(_controller: ScheduledController, env: Env): Promise<void> {
		const results = await Promise.all(TARGETS.map((t) => checkUrl(t)));
		await saveResults(env.DB, results);
	},
};
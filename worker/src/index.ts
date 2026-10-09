import { checkUrl } from "./checker";
import { TARGETS } from "./targets";

export default {
  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);

    if (url.pathname === "/check") {
      const results = await Promise.all(TARGETS.map((t) => checkUrl(t)));
      return Response.json(results);
    }

    return new Response("Pulse is running. Try /check", { status: 200 });
  },
};
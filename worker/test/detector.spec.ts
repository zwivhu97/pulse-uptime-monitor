import { expect, it } from "vitest";
import { isOutage } from "../src/detector";

const up = { is_up: 1 };
const down = { is_up: 0 };

it("is not an outage without enough history", () => {
	expect(isOutage([down, down], 3)).toBe(false);
});

it("is an outage after three failures in a row", () => {
	expect(isOutage([down, down, down], 3)).toBe(true);
});

it("is not an outage when a success breaks the streak", () => {
	expect(isOutage([down, up, down], 3)).toBe(false);
});

it("recovers as soon as the newest check is up", () => {
	expect(isOutage([up, down, down, down], 3)).toBe(false);
});
# Architecture

## Purpose

Pulse Uptime Monitor periodically checks public endpoints, records their
availability and latency, detects outages, sends alerts, and presents current
service health on a status page.

## Planned components

- **Checker service (`services/checker/`)** — a Cloud Run service responsible
  for performing endpoint checks.
- **Infrastructure (`infra/`)** — Terraform configuration for provisioning
  cloud resources.
- **Status page (`status-page/`)** — a static page that presents service health.
- **CI/CD (`.github/workflows/`)** — GitHub Actions workflows for validating
  and deploying project components.

## Planned data flow

1. A schedule triggers endpoint checks.
2. The checker requests each configured endpoint and captures its result and
   latency.
3. Results are made available to the status page, and detected outages can
   trigger notifications.

The scheduling mechanism, persistence layer, alerting integrations, and exact
deployment topology have not yet been selected. Record those choices in
[`decisions.md`](decisions.md) before implementation depends on them.

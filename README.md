# pulse-uptime-monitor

Serverless uptime and latency monitor for checking public endpoints on a
schedule, detecting outages, sending alerts, and serving a live status page.
Infrastructure as code and CI/CD are planned.

## Repository layout

```text
docs/                   Architecture and decision records
services/checker/       Cloud Run service for endpoint checks
infra/                  Terraform (planned)
status-page/             Static status page (planned)
.github/workflows/       CI/CD workflows (planned)
```

## Project status

This repository currently contains the project skeleton and planning documents.
Implementation details and technology choices are recorded in
[`docs/decisions.md`](docs/decisions.md) as they are made.

## Documentation

- [Architecture](docs/architecture.md)
- [Decisions](docs/decisions.md)

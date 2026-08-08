# Pulse Roadmap

## Overview

Pulse is being developed incrementally from a lightweight Python system monitor into a production-style infrastructure monitoring and observability platform.

The roadmap prioritises monitoring, observability, alerting, testing, deployment, and maintainability.

---

## Current Release

### v2.3.1 — Grafana Dashboard

**Status: Complete**

Current capabilities include:

- CPU monitoring
- Memory monitoring
- Disk monitoring
- System uptime
- Warning and critical thresholds
- Slack alerts
- Email alerts
- Alert cooldowns
- Recovery notifications
- Structured logging
- FastAPI health endpoint
- Prometheus metrics
- Prometheus scraping
- Grafana integration
- CPU dashboard panel
- Memory dashboard panel
- Disk dashboard panel
- Uptime dashboard panel
- Docker Compose
- GitHub Actions CI

---

## v2.3.2 — Alerting Improvements

**Status: Planned**

Focus:

Improve the structure, consistency, and maintainability of operational alerts.

Potential work includes:

- Structured alert representation
- Consistent alert formatting
- Severity classification
- Improved alert metadata
- Incident identifiers
- Improved operational logging

Implementation details will be finalised during development rather than treated as fixed requirements.

---

## v2.4 — Testing

**Status: Planned**

Introduce automated testing for core Pulse behaviour.

Areas to cover:

- Health endpoint
- Metrics endpoint
- Threshold evaluation
- Alert behaviour
- Recovery behaviour
- Configuration
- API responses

---

## v2.5 — Production Configuration

**Status: Planned**

Improve deployment and runtime configuration.

Potential work:

- Configuration validation
- Improved secret handling
- Logging configuration
- Environment-specific configuration
- Docker improvements
- Deployment documentation

---

## Future Development

Longer-term areas of exploration include:

- Alert history
- Incident tracking
- Additional notification providers
- Network monitoring
- Container monitoring
- Historical analysis
- Multi-host monitoring
- Cloud deployment
- Expanded Grafana dashboards

---

## v3.0 — Multi-Host Monitoring

**Status: Future**

The long-term direction for Pulse is to move beyond monitoring a single environment.

Potential capabilities include:

- Multiple monitored hosts
- Host identification
- Centralised metrics
- Host-specific dashboards
- Service availability monitoring
- Centralised alert management

The scope of v3.0 will be defined after the current monitoring platform is stable.

---

## Development Principles

Future Pulse development should continue to prioritise:

1. Reliability
2. Observability
3. Maintainability
4. Testability
5. Clear documentation
6. Incremental development

New features will solve a clear monitoring or operational problem rather than being added solely to increase the scope of the project.
# Pulse Roadmap

## Overview

Pulse is being developed incrementally from a lightweight Python system monitor into a production-style infrastructure monitoring and observability platform.

The roadmap prioritises monitoring, observability, alerting, testing, deployment, reliability, and maintainability.

---

## Current Release

### v2.3.2 — Modular Architecture Refactor

**Status: Complete**

Pulse has been reorganised from a simple Python application structure into a modular package architecture.

This release focuses on maintainability, separation of concerns, and preparing the application for its final testing and production-hardening phases.

### Completed

- Introduced the `app/` application package
- Separated API functionality into `app/api/`
- Separated monitoring functionality into `app/monitoring/`
- Separated alerting functionality into `app/alerts/`
- Separated logging functionality into `app/logging/`
- Separated dashboard functionality into `app/dashboard/`
- Moved Prometheus configuration into `config/`
- Updated internal Python imports
- Updated FastAPI application paths
- Updated Docker configuration for the modular application structure
- Updated Docker Compose configuration paths
- Updated backend CI imports for the new package structure
- Preserved existing monitoring and observability behaviour
- Updated repository documentation and project structure

### Current Platform Capabilities

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
- Prometheus-compatible metrics
- Prometheus scraping
- Grafana integration
- CPU dashboard panel
- Memory dashboard panel
- Disk dashboard panel
- Uptime dashboard panel
- Docker Compose deployment
- GitHub Actions backend CI

---

## Previous Release

### v2.3.1 — Grafana Dashboard

**Status: Complete**

Introduced the initial Grafana infrastructure dashboard connected to the existing Prometheus monitoring stack.

Completed dashboard panels:

- CPU usage
- Memory usage
- Disk usage
- System uptime

This release completed the core Pulse monitoring and observability stack.

---

## v2.3.3 — Alerting Improvements

**Status: Planned**

### Focus

Improve the structure, consistency, reliability, and maintainability of operational alerts.

Potential work includes:

- Structured alert representation
- Consistent alert formatting
- Severity classification
- Improved alert metadata
- Incident identifiers
- Improved operational logging
- Alert failure handling
- Cooldown reliability
- Recovery notification reliability

Implementation details will be finalised during development rather than treated as fixed requirements.

---

## v2.4.0 — Testing

**Status: Planned**

Introduce broader automated testing for core Pulse behaviour.

### Areas to Cover

- Health endpoint
- Metrics endpoint
- System metric collection
- Threshold evaluation
- Warning behaviour
- Critical behaviour
- Alert behaviour
- Alert cooldowns
- Recovery behaviour
- Configuration
- API responses

Testing should prioritise behaviour that could cause incorrect monitoring or alerting rather than testing implementation details.

---

## v2.5.0 — Production Configuration

**Status: Planned**

Improve deployment, runtime configuration, and operational reliability before Pulse moves primarily into maintenance.

### Potential Work

- Configuration validation
- Improved secret handling
- Logging configuration
- Environment-specific configuration
- Docker improvements
- Docker validation in CI
- Container health checks
- Failure handling
- Deployment documentation
- Final operational review

---

## Stable / Maintenance Phase

After the v2.5.0 production-hardening work is complete, Pulse will move primarily into maintenance.

Development during this phase will focus on:

- Bug fixes
- Dependency updates
- Security updates
- Monitoring reliability
- Documentation maintenance
- Small operational improvements
- Portfolio maintenance

Large new features will generally be deferred to the v3.0.0 roadmap.

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

These features are exploratory and are not required before Pulse enters maintenance.

---

## v3.0.0 — Multi-Host Monitoring

**Status: Future**

The long-term direction for Pulse is to move beyond monitoring a single environment and explore centralised infrastructure monitoring.

Potential capabilities include:

- Multiple monitored hosts
- Host identification
- Centralised metrics
- Host-specific dashboards
- Service availability monitoring
- Centralised alert management

The scope of v3.0.0 will be defined after the current monitoring platform is stable and there is a clear engineering reason to expand beyond single-environment monitoring.

---

## Development Principles

Future Pulse development will continue to prioritise:

1. Reliability
2. Observability
3. Maintainability
4. Testability
5. Clear documentation
6. Incremental development

New features should solve a clear monitoring or operational problem rather than being added solely to increase the scope of the project.
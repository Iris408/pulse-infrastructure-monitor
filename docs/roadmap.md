# Pulse Roadmap

## Overview

Pulse is a production-style infrastructure monitoring and observability project built with Python, FastAPI, Prometheus, Grafana, and Docker.

The core monitoring platform is complete. Pulse is now moving into maintenance, with future work focused on reliability, testing, security, dependency management, documentation, and small operational improvements rather than continued feature expansion.

---

## Current Release

### v2.3.2 — Modular Architecture Refactor

**Status: Complete**  
**Lifecycle: Maintenance**

v2.3.2 reorganised Pulse into a modular application architecture, completing the current planned feature cycle.

The refactor improved separation of concerns across monitoring, API, alerting, logging, and dashboard functionality while preserving the existing monitoring and observability behaviour.

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
- Updated Docker configuration
- Updated Docker Compose configuration paths
- Updated backend CI for the modular structure
- Preserved existing monitoring and observability behaviour
- Updated repository documentation and project structure

---

## Current Platform Capabilities

Pulse currently provides:

- CPU monitoring
- Memory monitoring
- Disk monitoring
- System uptime monitoring
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

## Release History

### v2.3.1 — Grafana Dashboard

**Status: Complete**

Introduced the initial Grafana infrastructure dashboard connected to the Prometheus monitoring stack.

Completed dashboard panels:

- CPU usage
- Memory usage
- Disk usage
- System uptime

This release completed the core Pulse monitoring and observability stack.

### v2.3.2 — Modular Architecture Refactor

**Status: Complete**

Reorganised Pulse into dedicated application modules for:

- API
- Monitoring
- Alerting
- Logging
- Dashboard integration

This established a cleaner architecture for long-term maintenance and testing.

---

## Maintenance Roadmap

Future Pulse development is intentionally limited to maintenance and reliability work.

### Testing

Planned improvements include:

- Health endpoint tests
- Metrics endpoint tests
- System metric collection tests
- Threshold evaluation tests
- Warning and critical behaviour tests
- Alert behaviour tests
- Alert cooldown tests
- Recovery notification tests
- Configuration tests
- API response tests

Testing should prioritise behaviour that could cause incorrect monitoring or alerting rather than implementation details.

### Alert Reliability

Maintenance work may include:

- Consistent alert formatting
- Improved alert metadata
- Alert failure handling
- Cooldown reliability
- Recovery notification reliability
- Operational logging improvements

These are reliability improvements rather than a new alerting feature cycle.

### CI and Security

Planned maintenance improvements may include:

- Docker validation in CI
- Dependency review
- Automated security analysis
- Dependency updates
- Python version maintenance
- Workflow updates

### Configuration and Infrastructure

Maintenance work may include:

- Configuration validation
- Secret-handling improvements
- Logging configuration
- Docker improvements
- Container health checks
- Failure handling
- Deployment documentation

### Documentation

Documentation will be maintained alongside technical changes, including:

- Setup instructions
- Architecture documentation
- Monitoring configuration
- Alert configuration
- Troubleshooting guidance
- Release notes

---

## Deliberately Out of Scope

The following capabilities are not part of the current Pulse roadmap:

- Multi-host monitoring
- Centralised host management
- Incident management platform
- Alert history platform
- Additional notification providers
- Network monitoring
- Container orchestration monitoring
- Historical analytics platform
- Cloud monitoring platform
- Large-scale distributed monitoring

These would significantly expand the scope of Pulse and are not required for the project to demonstrate infrastructure monitoring and observability engineering.

If a future engineering requirement provides a clear reason to revisit one of these areas, it will be evaluated as a separate major release rather than remaining permanently on the active backlog.

---

## Maintenance Principles

Pulse maintenance prioritises:

1. Reliability
2. Observability
3. Maintainability
4. Testability
5. Security
6. Clear documentation

New features should only be considered when they solve a clear monitoring or operational problem.

The objective is to keep Pulse stable, understandable, demonstrable, and maintainable rather than continually increasing its scope.
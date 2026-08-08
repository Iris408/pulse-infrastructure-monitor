# Learning Notes

## Overview

This document covers the key technical concepts, decisions, and lessons learned while building Pulse.

It's meant as a reference for future development, review and explaining the reasoning behind important choices made throughout the project.

---

# Monitoring & Observability

## Understanding System Metrics

One of the primary goals of Pulse was learning how infrastructure metrics can be collected and monitored in real time.

Key concepts learned were:

- CPU utilisation
- Memory usage
- Disk utilisation
- System uptime
- Health checks

Using the `psutil` library provided practical experience with collecting operating system metrics directly from Python.

---

## FastAPI for Operational APIs

Pulse uses FastAPI as a lightweight operational API rather than a traditional CRUD application.

This included building endpoints such as:

- `/`
- `/health`
- `/metrics`

These let external services to check the application's health and pull Prometheus-compatible metrics.

---

# Containerisation

Building Pulse gave me hands-on experience with Docker and Docker Compose.

Topics covered:

- Multi-service applications
- Container networking
- Docker volumes
- Environment variables
- Health checks

Running Prometheus, Grafana, and Pulse together showed how containerised services communicate on a shared network.

---

# Prometheus

A key milestone was understanding how Prometheus collects metrics.

Key concepts learned:

- Pull-based metric collection
- Metric scraping
- Prometheus configuration
- Time-series data
- `/metrics` endpoints

Instead of pushing metrics out, Pulse exposes them for Prometheus to then pull on a set schedule.

---

# Grafana

Grafana introduced dashboard-driven infrastructure monitoring.

Topics covered:

- Data sources
- Dashboard creation
- Time-series visualisation
- Operational dashboards
- Infrastructure

---

# Logging

Pulse introduced structured logging for monitoring events.

Lessons learned:

- Recording operational events
- Separating application logs from monitoring data
- Creating readable log files
- Improving troubleshooting through historical records

---

# Alerting

The project explored automated infrastructure notifications.

Current implementation includes:

- Slack alerts
- Email alerts
- Alert cooldowns
- Recovery notifications

This showed how monitoring systems can proactively notify operators when thresholds are exceeded.

---

# GitHub Actions

Pulse gave me practical experience with continuous integration.

Topics covered:

- Automated validation
- Python syntax checking
- Docker validation
- CI pipelines
- Build verification

Building CI workflows highlighted why every change should be validated before merging into the main branch.

---

# Docker Debugging

Throughout development, I ran into and resolved several Docker-related issues.

Examples include:

- Environment variable configuration
- Container networking
- Health check failures
- Docker Compose validation
- Volume persistence

These challenges deepened my understanding of how containerised applications behave in development environments.

---

# Documentation

One of the most valuable lessons was the importance of clear documentation.

The project now splits documentation into focused guides covering:

- Architecture
- Configuration
- Monitoring
- Alerting
- Deployment
- Troubleshooting

This keeps the README concise while still providing detailed technical references.

---

# Engineering Practices

The project reinforced several software engineering principles, including:

- Separation of concerns
- Modular design
- Incremental development
- Continuous integration
- Versioned releases
- Production-style project organisation

---

# Challenges

Key technical challenges during development included:

- Configuring Docker networking
- Integrating Prometheus with FastAPI
- Connecting Grafana to Prometheus
- Designing reusable monitoring components
- Managing environment variables
- Debugging CI workflows

Each challenge strengthened my understanding of modern backend and DevOps practices.

---

# Future Learning Goals

Future versions will explore:

- Automated testing with pytest
- Structured alert models
- Incident management
- Alert history
- Multiple notification providers
- Deployment automation
- Cloud-based monitoring
- Kubernetes deployment

---

# Reflection

Pulse has evolved from a terminal-based monitoring script into a production-style infrastructure monitoring platform.

Building it gave me practical experience across backend engineering, observability, Docker, monitoring, logging, continuous integration, and operational tooling.

The lessons learned throughout development continue to shape the architecture and engineering practices I use across other projects.
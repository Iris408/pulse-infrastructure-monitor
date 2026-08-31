# Learning Notes

## Overview

This document records the key technical concepts, engineering decisions, challenges, and lessons learned while building Pulse.

Pulse began as a lightweight Python system-monitoring project and gradually developed into a containerised infrastructure monitoring and observability platform using FastAPI, Prometheus, Grafana, Docker, structured logging, and automated CI.

These notes provide a reference for reviewing the project and explaining the reasoning behind important technical decisions.

---

# Monitoring & Observability

## Understanding System Metrics

One of the primary goals of Pulse was learning how infrastructure metrics can be collected and monitored using Python.

Key concepts included:

- CPU utilisation
- Memory usage
- Disk utilisation
- System uptime
- Health checks
- Monitoring thresholds

Using the `psutil` library provided practical experience with collecting operating system metrics directly from Python.

An important lesson was that collecting a metric is only one part of monitoring. The data also needs to be interpreted, exposed, logged, visualised, and potentially used to trigger operational alerts.

---

# FastAPI for Operational APIs

Pulse uses FastAPI as a lightweight operational API rather than as a traditional CRUD application.

The API includes endpoints such as:

- `/`
- `/health`
- `/metrics`

This provided experience building endpoints intended for infrastructure and monitoring systems rather than end-user application workflows.

The `/health` endpoint provides application health information, while `/metrics` exposes monitoring data in a Prometheus-compatible format.

This demonstrated how backend APIs can support operational infrastructure as well as traditional application functionality.

---

# Containerisation

Building Pulse provided hands-on experience with Docker and Docker Compose.

Topics included:

- Containerising a Python application
- Multi-service applications
- Container networking
- Docker volumes
- Environment configuration
- Container health checks
- Docker Compose

Running Pulse, Prometheus, and Grafana together demonstrated how independent containerised services can communicate through a shared Docker network.

It also reinforced the difference between host networking and container networking. Services inside Docker Compose can communicate using their service names rather than relying on `localhost`.

---

# Prometheus

A major milestone was learning how Prometheus collects and stores monitoring metrics.

Key concepts included:

- Pull-based metric collection
- Metric scraping
- Prometheus configuration
- Time-series metrics
- Scrape targets
- `/metrics` endpoints

Instead of Pulse pushing monitoring data directly to Prometheus, Pulse exposes metrics through its FastAPI `/metrics` endpoint.

Prometheus then periodically scrapes that endpoint.

The resulting flow is:

```text
Pulse
  │
  │ exposes /metrics
  ▼
Prometheus
  │
  │ stores/query metrics
  ▼
Grafana
```

This helped establish a clearer understanding of the role each component plays within an observability stack.

---

# Grafana

Grafana introduced dashboard-driven infrastructure monitoring.

Topics included:

- Configuring Prometheus as a data source
- Creating dashboard panels
- Querying monitoring metrics
- Visualising infrastructure data
- Persistent dashboard storage

The Pulse dashboard currently visualises:

- CPU usage
- Memory usage
- Disk usage
- System uptime

Connecting Grafana to Prometheus demonstrated how metric collection and metric visualisation can remain separate concerns.

---

# Logging

Pulse introduced structured logging for monitoring and alerting events.

Lessons included:

- Recording operational events
- Separating application logs from metric data
- Creating readable monitoring history
- Recording alert behaviour
- Recording cooldown events
- Recording recovery events
- Using logs for troubleshooting

Structured logging made it easier to understand not only the current state of the monitored system but also what Pulse had previously detected and how the application responded.

---

# Alerting

Pulse provided practical experience with automated infrastructure notifications.

The current implementation includes:

- Slack alerts
- Email alerts
- Warning and critical threshold behaviour
- Alert cooldowns
- Recovery notifications
- Structured alert logging

Implementing cooldown behaviour demonstrated why monitoring systems need to consider notification noise rather than simply sending an alert every time a threshold remains exceeded.

Recovery notifications also introduced the concept of monitoring state changes rather than only detecting failures.

---

# Modular Application Design

The v2.3.2 refactor provided practical experience restructuring an application after its scope had grown.

Pulse moved from a simpler Python application structure into dedicated packages for:

```text
app/
├── api/
├── monitoring/
├── alerts/
├── logging/
└── dashboard/
```

This reinforced several software engineering concepts:

- Separation of concerns
- Clear component responsibilities
- Modular Python application design
- Managing internal imports
- Refactoring without intentionally changing existing behaviour
- Updating infrastructure after application restructuring
- Keeping documentation aligned with architecture changes

One of the main lessons from the refactor was that project structure that works well for an early prototype may become harder to maintain as responsibilities increase.

Refactoring allowed the existing functionality to remain while making the codebase easier to understand and maintain.

---

# GitHub Actions

Pulse provided practical experience with continuous integration.

The current backend CI workflow introduced experience with:

- Automated backend validation
- Running checks on pushes and pull requests
- Python validation
- Protecting the main development branch from regressions
- Updating CI after application restructuring

Building and maintaining the workflow reinforced the value of automatically validating changes before they are merged.

Additional testing, security analysis, dependency checks, and Docker validation remain maintenance improvements rather than requirements for expanding the feature scope.

---

# Docker Debugging

Several Docker-related issues were encountered and resolved during development.

Areas that required debugging included:

- Environment variable configuration
- Container networking
- Health checks
- Docker Compose configuration
- Prometheus connectivity
- Grafana connectivity
- Persistent volumes
- Application paths after restructuring

These problems provided useful experience diagnosing failures across multiple services rather than debugging only application code.

A particularly important lesson was understanding that a successful application container does not automatically mean the complete monitoring stack is correctly connected.

Each relationship between Pulse, Prometheus, and Grafana also needs to function correctly.

---

# Configuration

Pulse provided experience separating runtime configuration from application source code.

Configuration areas included:

- Monitoring intervals
- Resource thresholds
- Slack integration
- Email integration
- Alert behaviour
- Docker configuration

Environment variables made it possible to change operational behaviour without modifying application code.

The project also reinforced the importance of keeping credentials and other sensitive configuration outside source control.

---

# Documentation

One of the most useful lessons from Pulse was the importance of maintaining documentation alongside the application.

The project documentation is separated into focused guides covering areas such as:

- Architecture
- Alerting
- Configuration
- Grafana
- Logging
- Monitoring
- Setup
- Troubleshooting
- Release history and maintenance

This allows the root README to provide a concise project overview while more detailed engineering information remains available within `docs/`.

The v2.3.2 architecture refactor also demonstrated why documentation needs to be reviewed after structural changes. Documentation can become inaccurate even when the application's behaviour remains unchanged.

---

# Engineering Practices

Pulse reinforced several software engineering practices:

- Separation of concerns
- Modular application design
- Incremental development
- Continuous integration
- Containerisation
- Configuration management
- Structured logging
- Observability
- Versioned releases
- Technical documentation
- Refactoring existing systems
- Maintaining clear project scope

The project also demonstrated that a portfolio project does not need continual feature expansion to remain technically useful.

Once the intended monitoring and observability scope is complete, reliability, testing, security, documentation, and maintenance become more valuable than continually adding new capabilities.

---

# Challenges

Key technical challenges during development included:

- Configuring Docker networking
- Integrating Prometheus with FastAPI
- Connecting Grafana to Prometheus
- Designing reusable monitoring components
- Implementing alert cooldown behaviour
- Managing environment variables
- Maintaining container health checks
- Debugging CI workflows
- Refactoring the application into modular packages
- Updating infrastructure paths after restructuring
- Keeping documentation aligned with implementation changes

Working through these challenges provided practical experience across backend engineering, infrastructure, observability, and DevOps workflows.

---

# Continued Learning

Pulse has reached the end of its current feature-development cycle, but it can continue to provide engineering practice through maintenance.

Useful maintenance areas include:

- Automated testing with `pytest`
- Testing monitoring and threshold behaviour
- Testing alert cooldown and recovery behaviour
- CI improvements
- Docker validation
- Dependency management
- Security analysis
- Configuration validation
- Alert reliability
- Operational debugging

These improvements strengthen the existing system without requiring Pulse to expand into a larger monitoring platform.

Technologies such as Kubernetes, distributed monitoring, cloud observability, and incident-management systems can be explored separately when another project provides a genuine reason to use them.

---

# Reflection

Pulse evolved from a terminal-based Python monitoring script into a production-style infrastructure monitoring and observability platform.

Building it provided practical experience across:

- Python backend development
- FastAPI
- System monitoring
- Prometheus
- Grafana
- Docker and Docker Compose
- Structured logging
- Slack and email alerting
- Continuous integration
- Modular application architecture
- Technical documentation

The project also demonstrated the value of incremental engineering. Each stage built on the previous one: metric collection became monitoring, monitoring gained alerting and logging, FastAPI exposed operational endpoints, Prometheus collected metrics, Grafana visualised them, Docker connected the services, and the final architecture refactor organised those responsibilities into a more maintainable structure.

Pulse now provides a useful reference project for infrastructure monitoring and observability concepts while remaining deliberately constrained enough to maintain effectively.
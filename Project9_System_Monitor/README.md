System_Monitor – Real-Time System Resource Monitoring and Alerting Tool

📌 Problem Statement (Project Objective):
As a DevOps engineer, you're responsible for maintaining the health and performance of systems running in production. Your task is to build a Python-based System Monitor that:

Periodically checks CPU, memory, disk, and network usage.

Triggers alerts (via email, log, or other notifications) if any usage crosses predefined thresholds.

Logs system health statistics regularly for auditing and troubleshooting.

Optionally exposes system metrics via an HTTP API for Prometheus/Grafana-style integration.

🛠️ Expected Features (Solution Requirements):
Resource Monitoring

Track real-time CPU %, Memory %, Disk %, and Network stats.

Set thresholds for each resource (e.g., CPU > 80%, Memory > 75%).

Logging Mechanism

Store logs with timestamps in a local file (e.g., system_monitor.log).

Include info like: timestamp, resource type, current usage, and alert status.

Alerting System

If thresholds are breached, trigger an alert:

Option 1: Send an email (using SMTP).

Option 2: Write an alert to a separate alerts.log.

Option 3: (Bonus) Send a Telegram or Slack message.

Automation & Scheduling

Run monitoring checks every N seconds/minutes (configurable).

Optionally use cron or schedule with schedule or APScheduler.

Configurable Thresholds

Allow user to customize limits for CPU, memory, etc., via a config file or CLI.

Extensibility (Optional)

Serve metrics via a simple REST API.

Export logs in JSON or CSV.

Add historical charts using matplotlib.

🎯 What DevOps Skills This Showcases:
Monitoring & Alerting (core DevOps responsibility)

Python scripting & automation

Resource usage tracking (similar to tools like Nagios/Prometheus)

Logging & incident response

Config management (YAML/INI/ENV file reading)

System performance tuning awareness


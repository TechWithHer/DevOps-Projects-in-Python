# 🖥️ System_Monitor – Real-Time System Resource Monitoring & Alerting Tool

A Python-based tool that monitors CPU, memory, disk, and network usage in real-time, logs system health, and triggers alerts when resource thresholds are breached.

## 🚀 Project Purpose

This project demonstrates essential DevOps capabilities, including system monitoring, logging, alerting, and automation. It's ideal for showcasing your scripting skills and understanding of infrastructure health tracking in real-time environments.

---

## 📌 Features

- ✅ Monitor CPU, Memory, Disk, and Network usage
- ⚠️ Alert via email or logs when thresholds are breached
- 🗂️ Log all resource stats with timestamps
- 🔁 Runs continuously or on schedule (configurable)
- 🛠️ Easy to configure thresholds (via CLI or config file)
- 🌐 (Optional) REST API for exposing metrics

---

## 🧠 Use Case Scenario

Imagine you are responsible for multiple EC2/Linux instances in production. One of them is becoming unresponsive. With this script:

- You are alerted when CPU spikes >80%
- You get logs that help pinpoint if it's a memory leak or I/O bottleneck
- You proactively resolve issues before users are impacted

---

## 🔧 Installation

```bash
git clone https://github.com/YourUsername/System_Monitor.git
cd System_Monitor
pip install -r requirements.txt
⚙️ Usage
bash
Copy
Edit
python3 system_monitor.py
You can optionally configure:

Check interval (e.g., every 30 seconds)

Alert thresholds

Notification method (Email, Log)

Output log file location

📝 Configuration
You can customize thresholds in config.yaml or via CLI args:

yaml
Copy
Edit
cpu_threshold: 80
memory_threshold: 75
disk_threshold: 90
network_threshold: 1000 # in KB/s
📂 Directory Structure
lua
Copy
Edit
System_Monitor/
├── system_monitor.py
├── config.yaml
├── logs/
│   └── system_monitor.log
├── alerts/
│   └── alerts.log
├── README.md
└── requirements.txt
📈 Sample Log Output
yaml
Copy
Edit
[2025-07-24 12:01:35] CPU: 45%, Memory: 67%, Disk: 40%
[2025-07-24 12:03:15] ALERT! CPU usage crossed 85%
📬 Optional Alerting
SMTP Email Alert

Telegram/Slack notification (Bonus)

Console + log file alert fallback

💡 Future Enhancements
Expose data via REST API

Grafana integration for live dashboards

Dockerize the tool for deployment

👨‍💻 Built With
Python 3

psutil – For resource usage stats

smtplib – For email alerts

schedule/APScheduler – For job scheduling

🧑‍💼 DevOps Concepts Demonstrated
System Monitoring & Alerting

Automation with Python

Threshold-based incident response

Logging & Resource Management

📣 Author
Ayushi Singh
GitHub: @TechWithHer
Building projects to bridge tech, automation, and DevOps.

📄 License
MIT License – feel free to use and modify.

yaml
Copy
Edit

---

Would you like me to generate a matching `config.yaml` template or define use-case-based alerts like low disk space on EC2?

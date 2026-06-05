# Network Monitoring and Alerting System

## Overview

The Network Monitoring and Alerting System is a Python-based web application designed to monitor network devices in real time. It continuously checks device availability using ICMP (ping), measures latency, tracks network status, and displays results through a web-based dashboard.

This project demonstrates practical skills in Networking, Python Development, Linux Administration, Database Management, and Web Development.

---

## Features

### Current Features

* Monitor network devices using ICMP Ping
* Display device status (UP/DOWN)
* Measure network latency
* Store monitoring results in SQLite database
* Web-based dashboard using Flask
* Automatic device health checks
* Historical monitoring records

### Planned Features

* Packet Loss Monitoring
* SNMP Monitoring
* CPU and Memory Utilization Tracking
* Interface Status Monitoring
* Email Alerts
* Telegram Notifications
* Interactive Charts and Graphs
* User Authentication
* Device Management Portal
* Network Topology Visualization

---

## Technologies Used

### Backend

* Python 3
* Flask

### Networking

* Ping3
* ICMP Monitoring

### Database

* SQLite

### Frontend

* HTML5
* CSS3
* Bootstrap (Future Enhancement)
* Chart.js (Future Enhancement)

### Development Environment

* Visual Studio Code
* Git
* Rocky Linux / Windows

---

## Project Structure

```text
Network-Monitor/

├── app.py
├── monitor.py
├── init_db.py
├── devices.json
├── database.db
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## System Architecture

```text
                 +------------------+
                 |  Web Dashboard   |
                 |     (Flask)      |
                 +--------+---------+
                          |
                          |
                 +--------v---------+
                 |   SQLite DB      |
                 +--------+---------+
                          ^
                          |
                 +--------+---------+
                 | Monitoring Engine|
                 |    (Ping3)       |
                 +--------+---------+
                          |
        -----------------------------------------
        |                  |                    |
        v                  v                    v
   Router/Switch      Server              Firewall
```

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd Network-Monitor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Initialization

Create the database:

```bash
python init_db.py
```

---

## Configure Devices

Edit `devices.json`

Example:

```json
[
  {
    "name": "Google DNS",
    "ip": "8.8.8.8"
  },
  {
    "name": "Cloudflare DNS",
    "ip": "1.1.1.1"
  }
]
```

---

## Running the Monitoring Engine

```bash
python monitor.py
```

This will:

* Ping configured devices
* Measure latency
* Determine UP/DOWN status
* Store results in SQLite

---

## Running the Web Dashboard

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## Dashboard Information

The dashboard displays:

| Field       | Description                  |
| ----------- | ---------------------------- |
| Device Name | Hostname of monitored device |
| IP Address  | Device IP Address            |
| Status      | UP or DOWN                   |
| Latency     | Response Time (ms)           |
| Last Check  | Timestamp of last check      |

---

## Future Improvements

### Monitoring

* SNMP Polling
* Interface Monitoring
* Bandwidth Utilization
* Packet Loss Analysis

### Alerts

* Email Notifications
* SMS Alerts
* Telegram Bot Integration

### Reporting

* Daily Reports
* Weekly Reports
* Uptime Statistics
* Historical Performance Graphs

### Security

* Login Authentication
* Role-Based Access Control
* Secure API Endpoints

---

## Learning Outcomes

This project helps develop knowledge in:

* Network Monitoring
* Linux Administration
* Python Programming
* Database Management
* Flask Web Development
* Network Troubleshooting
* Automation and Scripting
* SNMP Fundamentals

---

## Author

**Chetan Komawar**

Aspiring Network Engineer | Python Enthusiast | Linux & Networking Learner

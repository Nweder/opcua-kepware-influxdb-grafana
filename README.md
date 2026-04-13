README för vbg-local-server
# OPC-UA Machine Monitoring System – Local VBG Server Setup

This project presents a real-time data pipeline for industrial machine monitoring, developed as part of a bachelor thesis.

The system collects machine-related data from an OPC UA server through Kepware, processes it using Python, stores it in a local InfluxDB instance, and visualizes it in Grafana.

This branch (`vbg-local-server`) contains the **local / on-premise version** of the project.

## System Architecture

OPC UA (Kepware) → Python Data Collection Script → InfluxDB (Local) → Grafana (Local)

## Local Deployment Overview

This version is intended for local execution in a controlled environment or server-based setup where data is handled on-premise.

It is suitable for:
- industrial environments with restricted external network access
- local testing and validation
- full control over data flow and configuration

## How to Run the Local Setup

### Step 1 – Start Data Collection

Open Command Prompt or PowerShell:

```bash
cd C:\Users\_opcadm\Desktop\opcua-kepware-influxdb-grafana-main
python poll_kepware.py

This starts:

connection to the OPC UA / Kepware server
collection of machine-related data
transfer of collected values to InfluxDB
Step 2 – Start InfluxDB
cd C:\Users\_opcadm\Desktop\influxdb2-2.8.0-windows_amd64
influxd

Open in browser:

http://localhost:8086

Login:

Username: admin
Password: admin123
Step 3 – Start Grafana
cd C:\Users\_opcadm\Desktop\grafana-12.4.2\bin
grafana-server

Open in browser:

http://localhost:3000

Login:

Username: admin
Password: admin123
Dashboard Purpose

The Grafana dashboard can be used to visualize selected machine-related values such as:

machine running state
waiting states
warnings and errors
cutting hours
other selected machine signals

This supports a clearer overview of machine behavior and can contribute to maintenance-related monitoring.

Technologies
Python
OPC UA
Kepware
InfluxDB
Grafana
Branch Information

This repository contains two separate setup variants:

main → cloud-based version
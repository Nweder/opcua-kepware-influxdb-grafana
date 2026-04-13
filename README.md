# OPC-UA Machine Monitoring System

This project presents a real-time data pipeline for industrial machine monitoring, developed as part of a bachelor thesis.

The system collects machine-related data from an OPC UA-based source, processes it using Python, stores it in InfluxDB Cloud, and visualizes it in Grafana. The purpose of the solution is to support structured machine monitoring and maintenance-related follow-up in an industrial context.

## System Architecture

OPC UA / Kepware → Python Data Collection Script → InfluxDB Cloud → Grafana

## Overview

This branch (`main`) contains the **cloud-based version** of the project.

It is intended for:
- development
- testing
- cloud-based data storage
- remote visualization

A separate branch is available for the **local / on-premise VBG server setup**:

- `vbg-local-server` → local InfluxDB + local Grafana + VBG/local server configuration

## Cloud-Based Setup

In this version, the Python script collects machine-related data and writes it to InfluxDB Cloud. Grafana is then used to visualize the stored values.

This setup is suitable for:
- prototyping
- development
- remote access
- scalable monitoring environments

## Main Components

- **Python** for data collection and transfer
- **OPC UA / Kepware** as machine data source
- **InfluxDB Cloud** for time-series storage
- **Grafana** for visualization

## Project Purpose

The project was developed to demonstrate how machine-related data can be collected, transferred, stored, and visualized through a structured pipeline. The implemented solution supports monitoring of selected machine values and provides a basis for maintenance-related decision support.

## Deployment Variants

This repository contains two different setup variants:

- **`main`** → cloud-based version
- **`vbg-local-server`** → local / on-premise version for VBG server environment

## Technologies

- Python
- OPC UA
- Kepware
- InfluxDB Cloud
- Grafana
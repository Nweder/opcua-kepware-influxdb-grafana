# Solution 1 - Kepware -> Polling Script -> InfluxDB -> Grafana

This repository contains an MVP developed within a bachelor’s thesis project at University West, conducted in collaboration with VBG Group.

The purpose of the solution is to collect selected machine signals from Kepware, transfer them to InfluxDB, and support visualization in Grafana.

## Files
- `config.py` - configuration for Kepware and InfluxDB
- `poll_kepware.py` - reads selected tags from Kepware and forwards the data
- `writer.py` - writes data to InfluxDB
- `mock_kepware.py` - simulates a Kepware-like data source for testing
- `requirements.txt` - Python dependencies

## Configuration
Update `config.py` with the required Kepware and InfluxDB settings.

Grafana is used as the visualization layer for the stored data.

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
Run:
python poll_kepware.py
<<<<<<< HEAD
Branches
main contains the mock-based MVP solution
laser2-test contains the test setup for connection to the real Kepware environment
=======
```
>>>>>>> 82518bbee84772852cb12e4cd23d27e08e9dcaa0

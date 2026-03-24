# Solution 1 - Kepware -> Polling Script -> InfluxDB -> Grafana

This project is a minimal MVP for collecting machine-related signals from Kepware,
storing them in InfluxDB, and visualizing them in Grafana.

## Project files

- `config.py` - configuration for Kepware and InfluxDB
- `poll_kepware.py` - reads selected tags from Kepware REST Server
- `writer.py` - writes raw data to InfluxDB
- `requirements.txt` - required Python libraries

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt


2. Update configuration

Edit config.py and set:

Kepware base URL
Tag IDs
InfluxDB URL
token
org
bucket
# Kepware -> Polling Script -> InfluxDB -> Grafana

This repository is a small MVP that polls selected tags from Kepware (via the
Kepware REST endpoint), writes raw values to InfluxDB, and can be visualized in
Grafana.

Project files
- `config.py` — configuration for Kepware and InfluxDB (URL, token, tags).
- `poll_kepware.py` — polling loop that reads tags and forwards them to InfluxDB.
- `writer.py` — InfluxDB client wrapper to write points.
- `requirements.txt` — Python dependencies.

Quick start
1. Install dependencies:

```powershell
pip install -r requirements.txt
```

2. Edit `config.py` and set the correct values for:
- `KEPWARE_BASE_URL`
- `TAG_IDS`
- `INFLUX_URL`, `INFLUX_TOKEN`, `INFLUX_ORG`, `INFLUX_BUCKET`

3. Run the poller:

```powershell
python poll_kepware.py
```

Notes and recommendations
- The example uses `verify=False` for requests; only do this for local/self-signed certs.
- Do not keep production tokens in source control. Prefer environment variables
	or a `.env` file (use `python-dotenv`) and load them in `config.py`.
- `POLL_INTERVAL` is in seconds — adjust to your load and InfluxDB write capacity.
- `writer.py` attempts to store numeric values in `value` and falls back to `value_str`
	for non-numeric payloads.

If you want, I can:
- Add `.env` loading and update `config.py` to fetch secrets from environment variables.
- Add simple unit tests and a CI workflow.
- Improve logging and retry/backoff in `poll_kepware.py`.
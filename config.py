# Kepware REST Server base URL
# For local testing with the included mock server the default is set to
# http://localhost:5000. In production change this to your Kepware URL
# (for example: https://your-kepware:39320/iotgateway) or set the
# KEPWARE_BASE_URL environment variable.
import os

KEPWARE_BASE_URL = os.getenv("KEPWARE_BASE_URL", "http://localhost:5000")

# Tags/signals to read from Kepware
TAG_IDS = [
    "Channel1.Device1.temperature",
    "Channel1.Device1.run_signal",
    "Channel1.Device1.counter"
]

# InfluxDB settings
INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = "your-token"
INFLUX_ORG = "thesis"
INFLUX_BUCKET = "machine_data"

# Machine identifier
MACHINE_ID = "Machine_1"

# Poll interval in seconds
POLL_INTERVAL = 1

# JSON output (newline-delimited JSON). If set to None or empty string, JSON
# output to file is disabled. Otherwise the path is used and each poll will be
# appended as one JSON object per line.
JSON_OUTPUT_FILE = "data.jsonl"

# When testing locally without InfluxDB, set this to False to skip writes to Influx
# and only produce the JSON lines. Set to True to enable Influx writes.
WRITE_TO_INFLUX = False
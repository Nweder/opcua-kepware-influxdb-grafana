# Kepware REST Server base URL
KEPWARE_BASE_URL = "https://localhost:39320/iotgateway"

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
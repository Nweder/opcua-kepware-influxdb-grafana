from dotenv import load_dotenv
import os

load_dotenv()


KEPWARE_BASE_URL = "http://localhost:5000"

TAG_IDS = [
    "Channel1.Device1.temperature",
    "Channel1.Device1.run_signal",
    "Channel1.Device1.counter",
    "Channel1.Device1.pressure",
    "Channel1.Device1.alarm_code"
]


INFLUX_URL = "https://us-east-1-1.aws.cloud2.influxdata.com"
INFLUX_TOKEN = os.getenv("INFLUX_TOKEN")
INFLUX_ORG = "HV-Team"
INFLUX_BUCKET = "machine_data"
MACHINE_ID = "VBG_Cell_1"
POLL_INTERVAL = 1
JSON_OUTPUT_FILE = "data.jsonl"
WRITE_TO_INFLUX = True

print("Token loaded:", INFLUX_TOKEN is not None)
from dotenv import load_dotenv
import os

load_dotenv()

# we change it to VBG kepware server later ex :"https://IP-ADRESS:39320/iotgateway"
KEPWARE_BASE_URL = "http://localhost:5000"

# We need also to change tages later, these are just examples
TAG_IDS = [
    "Channel1.Device1.temperature",
    "Channel1.Device1.run_signal",
    "Channel1.Device1.counter",
    "Channel1.Device1.pressure",
    "Channel1.Device1.alarm_code"
]



# We don't need any more longer mock_kepware.py file, we can just change the URL to point to the real Kepware server and update the tag IDs as needed. The rest of the code will work the same way.

INFLUX_URL = "https://us-east-1-1.aws.cloud2.influxdata.com"
INFLUX_TOKEN = os.getenv("INFLUX_TOKEN")
INFLUX_ORG = "HV-Team"
INFLUX_BUCKET = "machine_data"
MACHINE_ID = "VBG_Cell_1"
POLL_INTERVAL = 1
JSON_OUTPUT_FILE = "data.jsonl"
WRITE_TO_INFLUX = True

# just to cleary that server working and token is loaded, we can remove this later
print("Token loaded:", INFLUX_TOKEN is not None)
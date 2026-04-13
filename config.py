from dotenv import load_dotenv
import os

load_dotenv()

# KEPWARE_BASE_URL = "http://localhost:5000"

# Real time tags 
TAG_IDS = [
    "ns=2;s=MachineStates.ProcessActive",
    "ns=2;s=MachineStates.WorkCount",
    "ns=2;s=MachineStates.WaitMaterialLoaded",
    "ns=2;s=MachineStates.WaitMaterialRemoved",
    "ns=2;s=MachineStates.WaitPartsSorted",
    "ns=2;s=MachineStates.WaitOther",
    "ns=2;s=SystemMessenger.ErrorCount",
    "ns=2;s=SystemMessenger.WarningCount",
    "ns=2;s=MaintenanceMessenger.ErrorCount",
    "ns=2;s=Work.CurrentJob",
    "ns=2;s=Work.CurrentPart",
    "ns=2;s=Machine.CuttingHours"
]

# Testing with mock server tags

# TAG_IDS = [
#     "Channel1.Device1.temperature",
#     "Channel1.Device1.run_signal",
#     "Channel1.Device1.counter",
#     "Channel1.Device1.pressure",
#     "Channel1.Device1.alarm_code"
# ]

INFLUX_URL = "https://us-east-1-1.aws.cloud2.influxdata.com"
INFLUX_TOKEN = os.getenv("INFLUX_TOKEN")
INFLUX_ORG = "HV-Team"
INFLUX_BUCKET = "machine_data"
# MACHINE_ID = "VBG_Cell_1"
MACHINE_ID = "Laser2"
POLL_INTERVAL = 1
JSON_OUTPUT_FILE = "data.jsonl"  # for testing, not used in production
WRITE_TO_INFLUX = True

# just to cleary that server working 
print("Token loaded:", INFLUX_TOKEN is not None)
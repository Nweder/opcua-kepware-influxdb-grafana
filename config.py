from dotenv import load_dotenv
import os

load_dotenv()

# KEPWARE_BASE_URL = "http://172.22.8.67:56000"

OPC_UA_URL = "opc.tcp.://172.22.8.67:56000"

# # KEPWARE_BASE_URL = "http://localhost:5000"

# Real time tags 
TAG_IDS = [
    "ns=2;s=MachineStates.ProcessActive",
    # "ns=2;s=MachineStates.WorkCount",
    "ns=2;s=MachineStates.WaitMaterialLoaded",
    "ns=2;s=MachineStates.WaitMaterialRemoved",
    "ns=2;s=MachineStates.WaitPartsSorted",
    "ns=2;s=MachineStates.WaitOther",
    "ns=2;s=SystemMessenger.ErrorCount",
    "ns=2;s=SystemMessenger.WarningCount",
    "ns=2;s=MaintenanceMessenger.ErrorCount",
    # "ns=2;s=Work.CurrentJob",
    # "ns=2;s=Work.CurrentPart",
    "ns=2;s=Machine.CuttingHours"
]

# # TAG_IDS = [
# #     "Channel1.Device1.temperature",
# #     "Channel1.Device1.run_signal",
# #     "Channel1.Device1.counter",
# #     "Channel1.Device1.pressure",
# #     "Channel1.Device1.alarm_code"
# # ]



# # We don't need any more longer mock_kepware.py file, we can just change the URL to point to the real Kepware server and update the tag IDs as needed. The rest of the code will work the same way.

INFLUX_URL = "https://us-east-1-1.aws.cloud2.influxdata.com"
INFLUX_TOKEN = os.getenv("INFLUX_TOKEN")
# INFLUX_TOKEN="u4wyUHTlSgSAc8z708OV5kUWI0Hg63bIk9OsIhbFYUK-o5AMYOUv4iuCfMCaW3WuNDFNAOl9kbOO9TDvhHPASA=="
# MACHINE_ID = "VBG_Cell_1"
INFLUX_ORG = "Hv-Team"
INFLUX_BUCKET = "machine_data"
MACHINE_ID = "Laser2"
POLL_INTERVAL = 1
# JSON_OUTPUT_FILE = "data.jsonl"
# WRITE_TO_INFLUX = False


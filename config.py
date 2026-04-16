from dotenv import load_dotenv
import os

load_dotenv()

OPC_UA_URL = "opc.tcp://YOUR_SERVER:56000"
 
# Real time tags 
TAG_IDS = [
    "ns=2;s=MachineStates.ProcessActive",
    "ns=2;s=MachineStates.WaitMaterialLoaded",
    "ns=2;s=MachineStates.WaitMaterialRemoved",
    "ns=2;s=MachineStates.WaitPartsSorted",
    "ns=2;s=MachineStates.WaitOther",
    "ns=2;s=SystemMessenger.ErrorCount",
    "ns=2;s=SystemMessenger.WarningCount",
    "ns=2;s=MaintenanceMessenger.ErrorCount",
    "ns=2;s=Machine.CuttingHours"
]

INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = os.getenv("INFLUX_TOKEN")
INFLUX_ORG = "HV-Team"
INFLUX_BUCKET = "machine_data"
MACHINE_ID = "Laser2"
POLL_INTERVAL = 1
WRITE_TO_INFLUX = True


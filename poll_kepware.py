from opcua import Client
from datetime import datetime
import time
from config import OPC_UA_URL, TAG_IDS, MACHINE_ID, POLL_INTERVAL
from writer import write_raw_data

client = Client(OPC_UA_URL)

try:
    client.connect()
    print("Connected to Laser2")

    nodes = {tag: client.get_node(tag) for tag in TAG_IDS}

    while True:
        timestamp = datetime.utcnow()

        for tag, node in nodes.items():
            try:
                value = node.get_value()
                print(tag, value)

                write_raw_data(MACHINE_ID, tag, value, timestamp)

            except Exception as e:
                print("Error:", tag, e)

        time.sleep(POLL_INTERVAL)

except Exception as e:
    print("Connection error:", e)

finally:
    client.disconnect()

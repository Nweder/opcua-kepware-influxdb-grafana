# from influxdb_client import InfluxDBClient, Point, WritePrecision
# from influxdb_client.client.write_api import SYNCHRONOUS
# from config import INFLUX_URL, INFLUX_TOKEN, INFLUX_ORG, INFLUX_BUCKET

# client = InfluxDBClient(
#     url=INFLUX_URL,
#     token=INFLUX_TOKEN,
#     org=INFLUX_ORG,
#     verify_sal=False
# )

# write_api = client.write_api(write_options=SYNCHRONOUS)


# def write_raw_data(machine_id, signal_name, value, timestamp):
#     try:
#         point = (
#             Point("machine_data")
#             .tag("machine_id", machine_id)
#             .tag("signal_name", signal_name)
#         )

#         # FIX: hantera text vs nummer
#         if isinstance(value, (int, float)):
#             point = point.field("value", float(value))
#         else:
#             point = point.field("value_str", str(value))

#         point = point.time(timestamp, WritePrecision.NS)

#         write_api.write(bucket=INFLUX_BUCKET, record=point)

#     except Exception as e:
#         print("Influx error:", e)




# Locala lagring test::
import json

def write_raw_data(machine_id, signal_name, value, timestamp):
    data = {
    "machine_id": machine_id,
    "signal": signal_name,
    "value": value,
    "timestamp": str(timestamp)
    }

    with open("data.jsonl", "a") as f:
        f.write(json.dumps(data) + "\n")

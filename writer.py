from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from config import INFLUX_URL, INFLUX_TOKEN, INFLUX_ORG, INFLUX_BUCKET

client = InfluxDBClient(
    url=INFLUX_URL,
    token=INFLUX_TOKEN,
    org=INFLUX_ORG
)

write_api = client.write_api(write_options=SYNCHRONOUS)


def write_raw_data(machine_id, signal_name, value, timestamp, quality="good"):
    point = (
        Point("machine_data")
        .tag("machine_id", machine_id)
        .tag("signal_name", signal_name)
        .tag("quality", quality)
        .field("value", float(value))
        .time(timestamp, WritePrecision.NS)
    )

    write_api.write(
        bucket=INFLUX_BUCKET,
        org=INFLUX_ORG,
        record=point
    )
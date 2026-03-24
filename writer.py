from influxdb_client import InfluxDBClient, Point, WritePrecision
from config import INFLUX_URL, INFLUX_TOKEN, INFLUX_ORG, INFLUX_BUCKET
from datetime import datetime

# Create client at module import (simple approach). If you prefer lazy
# initialization or retries, consider moving this into a factory function.
client = InfluxDBClient(
    url=INFLUX_URL,
    token=INFLUX_TOKEN,
    org=INFLUX_ORG
)

write_api = client.write_api()


def _parse_timestamp(ts):
    """Return a datetime when possible, otherwise return original value.

    Accepts ISO-format strings or datetime objects.
    """
    if isinstance(ts, datetime):
        return ts
    if isinstance(ts, str):
        try:
            # datetime.fromisoformat handles most ISO strings (including offset/Z in modern Python)
            return datetime.fromisoformat(ts)
        except Exception:
            # Leave as-is; Influx client can also accept ISO strings in many cases
            return ts
    return ts


def write_raw_data(machine_id, signal_name, value, timestamp, quality="good"):
    """Writes one raw signal value to InfluxDB.

    This function attempts to store numeric values in the `value` field and
    falls back to storing a string in `value_str` if conversion fails. It also
    tries to parse ISO timestamps to datetime objects for more reliable time
    precision handling.
    """
    ts = _parse_timestamp(timestamp)

    point = (
        Point("machine_data")
        .tag("machine_id", machine_id)
        .tag("signal_name", signal_name)
        .tag("quality", quality)
    )

    # Prefer numeric field when possible
    try:
        numeric_value = float(value)
        point = point.field("value", numeric_value)
    except Exception:
        # Non-numeric values are stored as string fallback
        point = point.field("value_str", str(value))

    # Set time (datetime preferred). If parsing failed, the original value may
    # still be acceptable to the client.
    point = point.time(ts, WritePrecision.NS)

    write_api.write(
        bucket=INFLUX_BUCKET,
        org=INFLUX_ORG,
        record=point
    )
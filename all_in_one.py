from dotenv import load_dotenv
import os
import time
from datetime import datetime, timezone

import requests

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


def read_tags():
    params = [("ids", tag_id) for tag_id in TAG_IDS]

    response = requests.get(
        f"{KEPWARE_BASE_URL}/read",
        params=params,
        timeout=10
    )
    response.raise_for_status()
    return response.json()


def get_signal_name(tag_id):
    return tag_id.split(".")[-1]


def transform_tag(tag):
    tag_id = tag["id"]
    value = tag["v"]
    quality = str(tag.get("s", "good"))
    timestamp = datetime.now(timezone.utc).isoformat()

    return {
        "machine_id": MACHINE_ID,
        "signal_name": get_signal_name(tag_id),
        "value": value,
        "quality": quality,
        "timestamp": timestamp
    }


def write_to_influx(data):
    line_protocol = (
        f'machine_data,'
        f'machine_id={data["machine_id"]},'
        f'signal_name={data["signal_name"]},'
        f'quality={data["quality"]} '
        f'value={float(data["value"])}'
    )

    url = (
        f"{INFLUX_URL}/api/v2/write"
        f"?bucket={INFLUX_BUCKET}"
        f"&org={INFLUX_ORG}"
        f"&precision=ns"
    )

    headers = {
        "Authorization": f"Token {INFLUX_TOKEN}",
        "Content-Type": "text/plain; charset=utf-8",
        "Accept": "application/json"
    }

    response = requests.post(url, headers=headers, data=line_protocol, timeout=20)

    if response.status_code != 204:
        print("Influx write failed")
        print("Status:", response.status_code)
        print("Body:", response.text)
    else:
        print(
            f'Wrote: {data["signal_name"]}={data["value"]} '
            f'quality={data["quality"]}'
        )


def main():
    while True:
        try:
            tags = read_tags()

            for tag in tags:
                transformed_data = transform_tag(tag)
                write_to_influx(transformed_data)

        except Exception as error:
            print(f"Error: {error}")

        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()
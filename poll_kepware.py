import time
from datetime import datetime, timezone

import requests

from config import KEPWARE_BASE_URL, TAG_IDS, MACHINE_ID, POLL_INTERVAL, WRITE_TO_INFLUX, JSON_OUTPUT_FILE
from writer import write_raw_data
import json
import os


def read_tags():
    """
    Reads selected tags from Kepware REST Server.
    """
    params = [("ids", tag_id) for tag_id in TAG_IDS]

    response = requests.get(
        f"{KEPWARE_BASE_URL}/read",
        params=params,
        verify=False,   # For local/self-signed certificate testing
        timeout=10
    )
    response.raise_for_status()
    return response.json()


def get_signal_name(tag_id):
    """
    Extracts the signal name from a full Kepware tag id.
    Example:
    Channel1.Device1.temperature -> temperature
    """
    return tag_id.split(".")[-1]


def main():
    while True:
        try:
            tags = read_tags()

            # Current timestamp in UTC ISO format (one timestamp per poll)
            timestamp = datetime.now(timezone.utc).isoformat()

            # Build JSON payload for this poll (machine-level)
            payload = {
                "machine_id": MACHINE_ID,
                "timestamp": timestamp,
                "signals": {}
            }

            for tag in tags:
                tag_id = tag.get("id")
                value = tag.get("v")
                quality = str(tag.get("s", "good"))

                signal_name = get_signal_name(tag_id) if tag_id else ""

                # Add to JSON payload
                payload["signals"][signal_name] = {
                    "value": value,
                    "quality": quality
                }

                # Optionally write individual point to InfluxDB
                if WRITE_TO_INFLUX:
                    try:
                        write_raw_data(
                            machine_id=MACHINE_ID,
                            signal_name=signal_name,
                            value=value,
                            timestamp=timestamp,
                            quality=quality
                        )
                    except Exception as e:
                        # Don't let a write failure stop the whole poll; log and continue
                        print(f"Warning: failed to write to InfluxDB for {signal_name}: {e}")

            # If JSON output is enabled, append this poll as a single JSON line
            if JSON_OUTPUT_FILE:
                try:
                    # Ensure directory exists
                    os.makedirs(os.path.dirname(JSON_OUTPUT_FILE) or '.', exist_ok=True)
                    with open(JSON_OUTPUT_FILE, "a", encoding="utf-8") as fh:
                        fh.write(json.dumps(payload, default=str, ensure_ascii=False) + "\n")
                except Exception as e:
                    # Don't crash the poller for logging/file issues; print for now
                    print(f"Warning: failed to write JSON output: {e}")

            print("Data saved to InfluxDB.")

        except Exception as error:
            print(f"Error: {error}")

        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()
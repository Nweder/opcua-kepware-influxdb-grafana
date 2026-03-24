import time
from datetime import datetime, timezone

import requests

from config import KEPWARE_BASE_URL, TAG_IDS as DEFAULT_TAG_IDS, MACHINE_ID, POLL_INTERVAL, WRITE_TO_INFLUX, JSON_OUTPUT_FILE
from writer import write_raw_data
import json
import os


def read_tags():
    """
    Reads selected tags from Kepware REST Server.
    """
    # This function will be updated by the caller to pass the tags list.
    raise RuntimeError("read_tags should be called with a list of tag ids: read_tags(tags)")
    response.raise_for_status()
    return response.json()


def read_tags(tags):
    """
    Reads selected tags from Kepware REST Server using the provided tags list.
    """
    params = [("ids", tag_id) for tag_id in tags]

    response = requests.get(
        f"{KEPWARE_BASE_URL}/read",
        params=params,
        verify=False,   # For local/self-signed certificate testing
        timeout=10
    )
    response.raise_for_status()
    return response.json()


def _load_tags_file(path="tags.json"):
    """Load tag ids from a JSON file. If file missing, create with defaults.

    The file is expected to contain a JSON array of tag id strings.
    """
    try:
        if not os.path.exists(path):
            # create default tags file
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(DEFAULT_TAG_IDS, fh, indent=2)
            return list(DEFAULT_TAG_IDS)

        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
            if isinstance(data, list):
                return data
            else:
                print(f"Warning: {path} does not contain a JSON list, using defaults")
                return list(DEFAULT_TAG_IDS)
    except Exception as e:
        print(f"Warning: failed to load {path}: {e}")
        return list(DEFAULT_TAG_IDS)


def get_signal_name(tag_id):
    """
    Extracts the signal name from a full Kepware tag id.
    Example:
    Channel1.Device1.temperature -> temperature
    """
    return tag_id.split(".")[-1]


def main():
    # Load tags from file and watch for changes so tag list can be updated
    tags_file = "tags.json"
    current_tags = _load_tags_file(tags_file)
    try:
        last_mtime = os.path.getmtime(tags_file) if os.path.exists(tags_file) else None
    except Exception:
        last_mtime = None

    while True:
        try:
            # check if tags file changed
            try:
                mtime = os.path.getmtime(tags_file)
            except Exception:
                mtime = None
            if mtime and mtime != last_mtime:
                print("Detected change in tags.json, reloading tags")
                current_tags = _load_tags_file(tags_file)
                last_mtime = mtime

            tags = read_tags(current_tags)

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
import time
from datetime import datetime, timezone
import requests

from config import KEPWARE_BASE_URL, TAG_IDS, MACHINE_ID, POLL_INTERVAL
from writer import write_raw_data


def read_tags():
    params = [("ids", tag_id) for tag_id in TAG_IDS]

    response = requests.get(
        f"{KEPWARE_BASE_URL}/read",
        params=params,
        verify=False,
        timeout=10
    )
    response.raise_for_status()
    return response.json()


def get_signal_name(tag_id):
    return tag_id.split(".")[-1]


def main():
    while True:
        try:
            tags = read_tags()

            for tag in tags:
                tag_id = tag["id"]
                value = tag["v"]
                quality = str(tag.get("s", "good"))
                timestamp = datetime.now(timezone.utc).isoformat()

                signal_name = get_signal_name(tag_id)

                write_raw_data(
                    machine_id=MACHINE_ID,
                    signal_name=signal_name,
                    value=value,
                    timestamp=timestamp,
                    quality=quality
                )

                print(f"Wrote: {signal_name}={value} quality={quality}")

        except Exception as error:
            print(f"Error: {error}")

        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()
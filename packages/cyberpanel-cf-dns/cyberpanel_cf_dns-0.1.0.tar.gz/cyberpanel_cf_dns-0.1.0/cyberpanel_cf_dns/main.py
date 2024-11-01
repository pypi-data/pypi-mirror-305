import json
import os
from datetime import datetime
from typing import List

from cloudflare import Cloudflare, CloudflareError, InternalServerError, NotFoundError
from cloudflare.pagination import SyncV4PagePagination
from cloudflare.types.dns import Record
from cloudflare.types.zones import Zone
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.environ.get("API_KEY")
API_TOKEN = os.environ.get("API_TOKEN")
API_EMAIL = os.environ.get("EMAIL")
ZONE_NAME = os.environ.get("ZONE_NAME")


def get_zone(client: Cloudflare) -> Zone | None:
    for zone in client.zones.list():
        if zone.name == ZONE_NAME:
            return zone

    print(f"{ZONE_NAME}: Zone not found")
    return None


def get_dns_records(client: Cloudflare, zone_id: str) -> List[Record]:
    try:
        records_info: SyncV4PagePagination = client.dns.records.list(zone_id=zone_id)
        all_records: List[Record] = []

        while records_info.has_next_page():
            records: List[Record] = [record for record in records_info]
            all_records.extend(records)
            records_info = records_info.get_next_page()

        print("Done")
        return all_records

    except NotFoundError:
        print("Zone not found")
        return []

    except Exception as e:
        print(f"Failed to retrieve DNS records: {e} - {e.message}")
        return []


# Custom function to handle datetime serialization
def datetime_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


def main(**kwargs) -> None:
    # if not any([API_EMAIL, API_KEY]):
    #     print("[X] API Key or Email not provided")
    #     return

    # if not ZONE_NAME:
    #     print("[X] Zone Name not provided")
    #     return

    # if not API_TOKEN:
    #     print("[X] API Token not provided")
    #     return

    client = Cloudflare(api_token=API_TOKEN)

    print("[+] Getting Zone...  ", end="")
    zone = get_zone(client)
    print(zone.name)

    print("[+] Getting DNS Records...  ", end="")
    dns_records: List[Record] = get_dns_records(client, zone_id=zone.id)

    if "list_records" in kwargs and kwargs["list_records"] == True:
        for record in dns_records:
            print(f"{record.type:<8}: {record.name} -> {record.content}")
            breakpoint()

    if "save_records" in kwargs and kwargs["save_records"] == True:
        serialized_records = [record.model_dump() for record in dns_records]
        datenow = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        filename = f"cf_records_{ZONE_NAME}_{datenow}.json"
        with open(filename, "w") as file:
            json.dump(serialized_records, file, default=datetime_serializer)
            print(f"[+] Records saved to {filename}")


if __name__ == "__main__":
    main()

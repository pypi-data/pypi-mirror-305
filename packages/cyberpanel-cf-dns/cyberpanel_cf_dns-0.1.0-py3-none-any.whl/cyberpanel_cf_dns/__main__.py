from argparse import ArgumentParser

from .main import main


def entrypoint():
    parser = ArgumentParser(
        description="CyberPanel Cloudflare DNS Sync",
        usage="python -m cyberpanel_cf_dns",
    )

    parser.add_argument(
        "--list-records",
        help="List cloudflare records",
        required=False,
        action="store_true",
    )

    parser.add_argument(
        "--dump-records",
        help="Save cloudflare records to a file",
        required=False,
        action="store_true",
    )

    args = parser.parse_args()

    if not args.list_records and not args.dump_records:
        parser.print_help()
        return
    if args.list_records:
        main(list_records=True)

    if args.dump_records:
        main(save_records=True)


if __name__ == "__main__":
    entrypoint()

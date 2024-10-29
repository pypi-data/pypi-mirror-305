import argparse

from yuumi.debrid import RealDebridAPI


def main():
    parser = argparse.ArgumentParser(
        description="Yuumi - Interact with the Real-Debrid API to manage your downloads, check instant availability of torrents, unrestrict links, and get user information.",
        epilog="Examples:\n"
               "  python yuumi.py --token 1234567890 --user\n"
               "  python yuumi.py --token 1234567890 --cached 2f5a5ccb7dc32b7f7d7b150dd6efbce87d2fc371\n"
               "  python yuumi.py --token 1234567890 --link https://example.com/download\n"
               "  python yuumi.py --token 1234567890 --download 1234567890\n"
               "  python yuumi.py --token 1234567890 --uncached 1234567890",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--token", "-t", type=str, required=True, help="Real-Debrid API access token")
    parser.add_argument("--user", "-u", action="store_true", help="Get user info")
    parser.add_argument("--cached", "-c", type=str, help="Check instantAvailability of an infohash")
    parser.add_argument("--link", "-l", type=str, help="Unrestrict a link")
    parser.add_argument("--download", "-d", type=str, help="Download a cached file")
    parser.add_argument("--uncached", "-uc", type=str, help="Download a non-cached file")
    args = parser.parse_args()

    api = RealDebridAPI(args.token)

    if args.cached:
        api.check_instant_availability(args.cached)
    elif args.link:
        api.unrestrict_link(args.link)
    elif args.download:
        api.download_cached(args.download)
    elif args.uncached:
        api.download_uncached(args.uncached)
    elif args.user:
        api.get_user_info()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
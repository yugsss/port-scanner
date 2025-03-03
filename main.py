import argparse
from scanner import scan_range
from utils import save_results, is_host_up

def main():
    parser = argparse.ArgumentParser(description="Advanced Python Port Scanner")
    parser.add_argument("host", help="Target IP or domain")
    parser.add_argument("--start", type=int, default=1, help="Start port")
    parser.add_argument("--end", type=int, default=1024, help="End port")
    parser.add_argument("--timeout", type=float, default=1.0, help="Timeout")
    parser.add_argument("--threads", type=int, default=50, help="Thread count")
    parser.add_argument("--verbose", action="store_true", help="Show closed ports")
    parser.add_argument("--save", action="store_true", help="Save scan result to file")

    args = parser.parse_args()

    if not is_host_up(args.host):
        print(f"[!] Host {args.host} appears to be down.")
        return

    results = scan_range(
        host=args.host,
        start=args.start,
        end=args.end,
        threads=args.threads,
        timeout=args.timeout,
        verbose=args.verbose
    )

    if args.save:
        save_results(results, args.host)

if __name__ == "__main__":
    main()

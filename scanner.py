from hasher import scan_port
from banner import grab_banner
from utils import load_common_ports
from concurrent.futures import ThreadPoolExecutor

def scan_range(host, start, end, threads=50, timeout=1.0, verbose=False):
    print(f"Scanning {host} from port {start} to {end}...\n")
    open_ports = []
    common_ports = load_common_ports()

    def task(port):
        is_open = scan_port(host, port, timeout)
        if is_open:
            banner = grab_banner(host, port, timeout)
            service = common_ports.get(str(port), "Unknown")
            print(f"[+] Port {port} ({service}) is OPEN - Banner: {banner or 'N/A'}")
            open_ports.append({
                "port": port,
                "service": service,
                "banner": banner or "N/A"
            })
        elif verbose:
            print(f"[-] Port {port} is closed")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for port in range(start, end + 1):
            executor.submit(task, port)

    return open_ports

import os
import json
import subprocess
import platform
from datetime import datetime

def is_host_up(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        subprocess.check_output(["ping", param, "1", host])
        return True
    except subprocess.CalledProcessError:
        return False

def save_results(data, host):
    os.makedirs("output", exist_ok=True)
    filename = f"output/scan_{host}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"\n[✔] Results saved to {filename}")

def load_common_ports(path="common_ports.json"):
    with open(path, "r") as f:
        return json.load(f)

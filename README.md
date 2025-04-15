# 🔍 Advanced Python Port Scanner

A lightweight, fast, and extensible Python-based port scanner that can scan a given IP or domain for open ports, detect running services, and optionally grab banners.

## 🚀 Features

- 🔢 Scan a range of ports (e.g., 1–1024)
- ✅ Check if a host is online before scanning
- ⚡ Fast scanning with multithreading
- 🔐 Detect common services by port number
- 🛠️ Grab service banners (optional, best effort)
- 📝 Save results to JSON file
- 👀 Verbose mode to see closed ports

## 📦 Project Structure
<pre> port-scanner/ 
  ├── main.py # CLI entry point 
  ├── scanner.py # Port scanning logic 
  ├── hasher.py # Socket port scanner 
  ├── banner.py # Banner grabbing 
  ├── utils.py # Host checking, saving, JSON loading 
  ├── common_ports.json # Known ports & services 
  ├── output/ # Output directory (auto-generated) 
  └── README.md # This page</pre>

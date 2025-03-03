import socket

def grab_banner(host, port, timeout=1.0):
    """Try to grab service banner from open port."""
    try:
        with socket.socket() as s:
            s.settimeout(timeout)
            s.connect((host, port))
            return s.recv(1024).decode(errors="ignore").strip()
    except:
        return None

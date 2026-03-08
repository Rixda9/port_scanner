import socket
import sys
def scan_port(host, port, timeout=0.5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
            return True
        except:
            return False
def main():
    if len(sys.argv) != 3:
        print("Usage: python port_scanner.py <host> <port-range>")
        print("Example: python port_scanner.py localhost 1-1000")
        sys.exit(1)
    host = sys.argv[1]
    port_range = sys.argv[2]
    b_port = int(port_range.split("-")[0])
    e_port = int(port_range.split("-")[1])
    print(f"Scanning {host} ports in the range {b_port}-{e_port}...")
    open_ports = []
    for i in range(b_port, e_port + 1):
        print(f"Scanning port {i}...", end="\r")
        if scan_port(host, i):
            open_ports.append(i)
    if open_ports:
        print(f"\nFound {len(open_ports)} open ports:")
        for port in open_ports:
            print(f"Port {port}: Open")
    else:
        print(f"\nNo open ports found")
if __name__ == "__main__":
    main()

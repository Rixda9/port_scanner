import socket 
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from ipaddress import ip_address

lock = Lock()
open_ports = []

def port_test(ip, port, timeout=3):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        if sock.connect_ex((ip, port)) == 0:
            try:
                # Infos about the port
                banner = sock.recv(1024).decode().strip()
            except:
                banner = "no banner"

            print(f"{port} is open - {banner}")
            # Avoid race conditions
            with lock:
                open_ports.append(port)


def ip_to_check(ip):
    try:
        ip_address(ip) 
        return ip
    except ValueError:
        raise ValueError("invalid ip")

def main():

    ip = ip_to_check(input("What ip do you want to test: "))
    try:
        start = int(input("Start port: "))
        end = int(input("End port: "))
        if start >= end:
            raise ValueError("Start port must be less than end port")
    except ValueError:
        raise ValueError("Enter valid numbers: ")

    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda p: port_test(ip, p), range(start, end + 1))
    print(f"\nFound {len(open_ports)} open ports")
if __name__ == "__main__":
    main()

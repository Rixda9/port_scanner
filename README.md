# Port Scanner

A simple TCP port scanner written in Python.

## Usage
```bash
python3 port_scanner.py <host> <port-range>
```

## Examples
```bash
python3 port_scanner.py google.com 80-443
python3 port_scanner.py localhost 1-1000
python3 port_scanner.py scanme.nmap.org 20-100
```

## How It Works

Uses Python sockets to attempt TCP connections to each port in the specified range. If connection succeeds, port is open.

## What I Learned

- Python socket programming
- Network scanning basics
- Command-line argument parsing
- Error handling with try/except

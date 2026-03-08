# Port Scanner

A simple TCP port scanner with threading and banner grabbing written in Python.

## Usage
```bash
python3 port_scanner.py

```

## Examples


```bash
# scanme.nmap.org (45.33.32.156) is a public host maintained by Nmap for testing
python3 port_scanner.py 
What ip do you want to test: 45.33.32.156
Start port: 20
End port: 1000
22 is open - SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
80 is open - no banner
```

## How It Works

Uses Python sockets to attempt TCP connections to each port in the specified range. If connection succeeds, port is open.

## What I Learned

- Race conditions
- Python socket programming
- Network scanning basics
- Error handling with try/except
- Banner grabbing
- Threading 

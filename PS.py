# port_scanner.py
# Author: Graywolf0
# 📌 Educational Project - For Portfolio Use

import socket

def scan_ports(target, start_port, end_port):
    print(f"\n🔍 Scanning {target} from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # hızlı tarama için timeout
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"✅ Port {port} is OPEN")
                open_ports.append(port)
            sock.close()
        except socket.error:
            print("❌ Could not connect to server")
            break

    if not open_ports:
        print("\nNo open ports found.")
    else:
        print(f"\nOpen ports: {open_ports}")


if __name__ == "__main__":
    print("🔐 Simple Port Scanner 🔐")
    target = input("Enter target IP or hostname: ")
    try:
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        scan_ports(target, start_port, end_port)
    except ValueError:
        print("⚠️ Please enter valid port numbers.")

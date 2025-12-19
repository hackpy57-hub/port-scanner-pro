import socket
import os
import time

def clear():
    os.system("clear" if os.name == "posix" else "cls")

clear()

banner = """
========================================
   🔎 PORT SCANNER PRO
   Educational Security Tool
   Author: hackpy57
========================================
"""
print(banner)

target = input("Enter IP or Domain to scan: ")

ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

print("\nScanning started...\n")
time.sleep(1)

for port in ports:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        s.close()
    except:
        pass

print("\n✔ Scan Complete")

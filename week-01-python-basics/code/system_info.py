"""
system_info.py

Purpose:
- Practice basic Python syntax
- Read system information
- Prepare for robotics scripts later
"""

import platform
import os

def main():
    print("=== Raspberry Pi System Info ===")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Machine: {platform.machine()}")
    print(f"Current User: {os.getlogin()}")

if __name__ == "__main__":
    main()

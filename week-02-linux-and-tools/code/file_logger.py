"""
file_logger.py

Purpose:
- Practice file I/O in Python
- Log information with timestamps
- Foundation for robotics sensor logging
"""

from datetime import datetime

LOG_FILE = "log.txt"

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as file:
        file.write(f"[{timestamp}] {message}\n")

def main():
    print("Simple File Logger")
    user_input = input("Enter a message to log: ")
    log_message(user_input)
    print("Message logged successfully.")

if __name__ == "__main__":
    main()

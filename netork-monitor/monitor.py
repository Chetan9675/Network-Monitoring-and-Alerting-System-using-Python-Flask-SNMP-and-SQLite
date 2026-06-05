import sqlite3
import json
from ping3 import ping
from datetime import datetime

with open("devices.json") as f:
    devices = json.load(f)

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

for device in devices:

    result = ping(device["ip"])

    if result:
        status = "UP"
        latency = round(result * 1000, 2)
    else:
        status = "DOWN"
        latency = 0

    cursor.execute("""
    INSERT INTO devices
    (name, ip, status, latency, last_check)
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        device["name"],
        device["ip"],
        status,
        latency,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

conn.commit()
conn.close()

print("Monitoring Complete")
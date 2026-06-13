import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("sysinsight.db")

df = pd.read_sql_query(
    "SELECT * FROM metrics",
    conn
)

conn.close()

# CPU

plt.figure(figsize=(10,4))
plt.plot(df["cpu"])
plt.title("CPU Usage Trend")
plt.ylabel("CPU %")
plt.grid(True)

# RAM

plt.figure(figsize=(10,4))
plt.plot(df["ram"])
plt.title("RAM Usage Trend")
plt.ylabel("RAM %")
plt.grid(True)

# Health

plt.figure(figsize=(10,4))
plt.plot(df["health"])
plt.title("System Health Trend")
plt.ylabel("Health Score")
plt.grid(True)

plt.show()
import sqlite3
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Read Database

conn = sqlite3.connect("sysinsight.db")

df = pd.read_sql_query(
    "SELECT * FROM metrics",
    conn
)

conn.close()

# Sample Numbers

X = np.arange(len(df)).reshape(-1,1)

# ------------------------
# CPU Prediction
# ------------------------

cpu_model = LinearRegression()
cpu_model.fit(X, df["cpu"])

future = np.array([[len(df)+5]])

cpu_prediction = cpu_model.predict(future)

# ------------------------
# RAM Prediction
# ------------------------

ram_model = LinearRegression()
ram_model.fit(X, df["ram"])

ram_prediction = ram_model.predict(future)

# ------------------------
# Health Prediction
# ------------------------

health_model = LinearRegression()
health_model.fit(X, df["health"])

health_prediction = health_model.predict(future)

print("\n===== AI Prediction =====\n")

print(
    f"Predicted CPU Usage    : {cpu_prediction[0]:.2f}%"
)

print(
    f"Predicted RAM Usage    : {ram_prediction[0]:.2f}%"
)

print(
    f"Predicted Health Score : {health_prediction[0]:.2f}%"
)
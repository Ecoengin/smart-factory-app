import streamlit as st
import pandas as pd
import numpy as np
import paho.mqtt.client as mqtt
import time

# Simulate login
st.sidebar.title("Login")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
if username != "admin" or password != "admin":
    st.warning("Enter admin/admin to log in")
    st.stop()

st.title("🏭 Smart Factory-as-a-Service")

# Dashboard KPIs
st.header("📊 Factory KPIs")
col1, col2, col3 = st.columns(3)
col1.metric("Energy (kWh)", "1,210", "-2.3%")
col2.metric("Uptime", "99.2%", "+0.1%")
col3.metric("Anomaly Alerts", "0", "🟢")

# Temperature chart
st.subheader("🔧 Machine Temperature")
temp = np.random.normal(loc=75, scale=5, size=10)
chart_data = pd.DataFrame(temp, columns=["Temp (°C)"])
st.line_chart(chart_data)

# Maintenance alerts
st.subheader("🛠️ Predictive Maintenance")
alerts = pd.DataFrame({
    "Machine": ["Pump A", "Compressor B"],
    "Issue": ["Bearing", "Seal"],
    "Confidence": ["88%", "75%"],
    "ETA (days)": [7, 12]
})
st.table(alerts)

# Simulated Digital Twin status
st.subheader("🧠 Digital Twin Status")
status = {"Compressor": "Running", "Fan Motor": "Idle", "Sensor A": "Connected"}
for k, v in status.items():
    st.write(f"**{k}**: {v}")

st.caption("Demo powered by Streamlit | MQTT integration placeholder")
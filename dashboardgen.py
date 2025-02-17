%%writefile dashboardgen.py
import streamlit as st
import pandas as pd
import random
import datetime
import plotly.graph_objs as go

def generate_fake_data():
    time = [datetime.datetime.now() - datetime.timedelta(seconds=i) for i in range(50)]
    motor_de_temp = [random.uniform(60, 80) for _ in range(50)]
    motor_de_bpfo = [random.uniform(0.1, 0.5) for _ in range(50)]

    df = pd.DataFrame({
        'Time': time,
        'Motor DETemp': motor_de_temp,
        'Motor DE BPFO': motor_de_bpfo,
    })
    return df

def get_overall_condition(measurements, thresholds):
    for measurement, threshold in zip(measurements, thresholds):
        if measurement > threshold:
            return 'orange'  # Or 'red' depending on your logic
    return 'green'  # If all measurements are within thresholds

st.title("Live Maintenance Dashboard")

data = generate_fake_data()
motor_condition = get_overall_condition([data.iloc[-1]['Motor DETemp'], data.iloc[-1]['Motor DE BPFO']], [85, 0.8])

st.header("Status")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Motor")
    st.write(f"Overall Condition: {motor_condition.upper()}")

st.header("Graphs")

motor_de_temp_graph = go.Figure(
    data=[go.Scatter(x=data['Time'], y=data['Motor DETemp'], mode='lines')],
    layout=go.Layout(title="Motor DE Temperature")
)
st.plotly_chart(motor_de_temp_graph)

motor_de_bpfo_graph = go.Figure(
    data=[go.Scatter(x=data['Time'], y=data['Motor DE BPFO'], mode='lines')],
    layout=go.Layout(title="Motor DE BPFO")
)
st.plotly_chart(motor_de_bpfo_graph)

if st.button("Refresh Data"):
    st.experimental_rerun()
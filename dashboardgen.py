import streamlit as st
import pandas as pd
import random
import datetime

st.title("Live Maintenance Dashboard")

# Corrected generate_fake_data function (same as before)
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

#... (rest of your code - thresholds, get_overall_condition - same as before)

# Status boxes
st.header("Status")
data = generate_fake_data()
motor_condition = get_overall_condition([data.iloc[-1]['Motor DETemp'], data.iloc[-1]['Motor DE BPFO']],
                                        [85, 0.8])  # Example thresholds

col1, col2 = st.columns(2)  # Create two columns for layout

with col1:
    st.subheader("Motor")
    st.write(f"Overall Condition: {motor_condition.upper()}")

# Graphs
st.header("Graphs")

motor_de_temp_graph = go.Figure(
    data=[go.Scatter(x=data['Time'], y=data['Motor DETemp'], mode='lines')],
    layout=go.Layout(title="Motor DE Temperature")
)

motor_de_bpfo_graph = go.Figure(
    data=[go.Scatter(x=data['Time'], y=data['Motor DE BPFO'], mode='lines')],
    layout=go.Layout(title="Motor DE BPFO")
)

st.plotly_chart(motor_de_temp_graph)
st.plotly_chart(motor_de_bpfo_graph)

# Refresh button (optional)
if st.button("Refresh Data"):
    st.experimental_rerun()
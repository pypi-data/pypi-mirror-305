import streamlit as st
from streamlit_slb_card import streamlit_slb_card
import json

# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run streamlit_slb_card/example.py`
st.set_page_config(layout='wide')
st.subheader("Streamlit Slb Card Examples")

# Create an instance of our component with a constant `name` arg, and
# print its output value.

total_violations = 12
beats_per_minutes = 100
high_risk_time_period_min = 1700
high_risk_time_period_max = 1900
total_quantity_of_emission = 184.6

col1, col2, col3, col4 = st.columns(4)

with col1:
    
    data = {
        "xAxis": ["Nov 1", "Nov 2", "Nov 3", "Nov 4", "Nov 5", "Nov 6"],
        "value": [2, 5.5, 2, 8.5, 1.5, 1],
        "color": "maroon"
    }
    
    result = streamlit_slb_card(
        title="Crew Health", 
        titleTextAlign="left",
        titleTextSize="25",
        headerContent=f"<div><div style='font-size:14px;font-weight: bold'>Average Pulse Rate</div><div><span style='font-size:40px'>{beats_per_minutes}</span> beats/min</div></div>",
        showChart=True,    
        chartType="LineChart", # Supported charts -> PieChart, coming soon
        chartTitle= "Violation Types",
        chartData=data
    )
    
with col2:
    data = [
        { "id": 0, "value": 10, "label": 'Helmet Violation', "color": 'green' },
        { "id": 1, "value": 32, "label": 'Coverall Violation', "color": 'red' },
        { "id": 2, "value": 45, "label": 'Glove Violation', "color": 'blue' },
        { "id": 3, "value": 28, "label": 'Vest Violation', "color": 'orange' }
    ]

    result = streamlit_slb_card(
        title="Crew Safety 123", 
        titleTextAlign="left",
        titleTextSize="25",
        headerContent=f"<div><div style='font-size:14px;font-weight: bold'>Total number of violations</div><div><span style='font-size:40px'>{total_violations}</span> violations</div></div>",
        showChart=True,    
        chartType="PieChart", # Supported charts -> PieChart, coming soon
        chartTitle= "Violation Types",
        chartData= data
    )

with col3:
    
    data = {
        "name": ["Total Wells", "Total Active", "Total Down"],
        "value": [45, 30, 15],
        "color": "green"
    }
    
    result = streamlit_slb_card(
        title="Site Security", 
        titleTextAlign="left",
        titleTextSize="25",
        headerContent=f"<div><div style='font-size:14px;font-weight: bold'>High-Risk time Period</div><div><span style='font-size:40px'>{high_risk_time_period_min} - {high_risk_time_period_max}</span> hours</div></div>",
        showChart=True,    
        chartType="BarChart", # Supported charts -> PieChart, coming soon
        chartTitle= "Violation Types",
        chartData=data
    )

with col4:
    
    data = {
        "xAxis": ["Nov 1", "Nov 2", "Nov 3", "Nov 4", "Nov 5", "Nov 6"],
        "value": [5, 15.5, 12, 18.5, 10.5, 4],
        "color": "blue"
    }
    
    result = streamlit_slb_card(
        title="Environment Monitoring", 
        titleTextAlign="left",
        titleTextSize="25",
        headerContent=f"<div><div style='font-size:14px;font-weight: bold'>Total Quantity Of Emission</div><div><span style='font-size:40px'>{total_quantity_of_emission}</span> kg/hr</div></div>",
        showChart=True,    
        chartType="LineChart", # Supported charts -> PieChart, coming soon
        chartTitle= "Violation Types",
        chartData=data
    )

# st.markdown("Result:" + state, unsafe_allow_html=True)


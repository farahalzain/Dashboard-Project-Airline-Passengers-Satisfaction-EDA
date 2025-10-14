import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from helper_functions import load_data

st.set_page_config(page_title="Service Impact", page_icon="🔧", layout="wide")
st.title("🔧 Service Impact on Satisfaction")

df = load_data()

# Select service columns present
service_cols = [
    'ease_of_online_booking','check_in_service','online_boarding','on_board_service',
    'seat_comfort','leg_room_service','cleanliness','food_and_drink',
    'in_flight_service','in_flight_wifi_service','in_flight_entertainment','baggage_handling'
]

st.subheader("🚀 Correlation heatmap (services vs satisfaction)")
# Prepare numeric satisfaction encoding: 1 if satisfied, 0 otherwise

df['satisfied_flag'] = df['satisfaction'].apply(lambda x: 1 if x=='Satisfied' else 0)


corr_df = df[service_cols + ["satisfied_flag"]].corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_df, annot=True, fmt=".2f", cmap="vlag", ax=ax)
st.pyplot(fig)

st.markdown("---")
st.subheader("⭐ Which services drive satisfaction the most?")
imp = corr_df["satisfied_flag"].drop("satisfied_flag").sort_values(ascending=False).reset_index()
imp.columns = ["service", "corr_with_satisfaction"]
st.dataframe(imp)

# Scatter for chosen service
service_choice = st.selectbox("Choose a service to inspect:", service_cols, index=0)
if service_choice:
    fig2 = px.box(df, x="satisfaction", y=service_choice, points="all", title=f"{service_choice} by Satisfaction")
    st.plotly_chart(fig2, use_container_width=True)


st.info('''💡
***Overall Insights***

**Top drivers of satisfaction:**

* Online Boarding
* In-Flight Entertainment


**Moderate drivers:**

* Seat Comfort
* On Board Service
* Leg_room Service
* Cleanliness

**Lesser (but still important) drivers:**

* In-Flight Wifi Service
* In-Flight Service
* Check In Service
* Baggage Handling
* Ease Online Booking
* Food & Drink

''')
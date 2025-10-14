import streamlit as st
import pandas as pd
import plotly.express as px
from helper_functions import load_data

st.set_page_config(page_title="Customer Loyalty", page_icon="🤝", layout="wide")
st.title("🤝 Customer Loyalty")

# Load data
df = load_data()
df["satisfaction"] = df["satisfaction"].astype(str).str.strip().str.lower()
df["customer_type"] = df["customer_type"].astype(str).str.strip().str.lower()

# Loyal vs First-time 
st.subheader("💙 Returning vs 🆕 First-time Satisfaction")

loyal_table = (
    df.groupby("customer_type")["satisfaction"]
      .apply(lambda x: (x == "satisfied").mean() * 100)
    .reset_index(name="satisfied_percent")
)

st.dataframe(loyal_table.round(2))

fig = px.bar(
    loyal_table,
    x="customer_type",
    y="satisfied_percent",
    title="😊 Satisfaction % by Customer Type",
    labels={"satisfied_percent": "% Satisfied", "customer_type": "Customer Type"},
    color="customer_type"
)
st.plotly_chart(fig, use_container_width=True)

# Which services matter most for Returning customers 
st.markdown("---")
st.subheader("⭐ What services matter most for Returning customers?")

# Filter returning customers only
returning_df = df[df["customer_type"] == "returning"]

service_cols = [
    'ease_of_online_booking','check_in_service','online_boarding','on_board_service',
    'seat_comfort','leg_room_service','cleanliness','food_and_drink',
    'in_flight_service','in_flight_wifi_service','in_flight_entertainment','baggage_handling'
]


# Encode satisfaction as binary
returning_df["satisfied_flag"] = (returning_df["satisfaction"] == "satisfied").astype(int)

# Compute absolute correlation with satisfaction
srv_corr = returning_df[service_cols + ["satisfied_flag"]].corr()["satisfied_flag"].drop("satisfied_flag")
srv_corr = srv_corr.abs().sort_values(ascending=False).reset_index()
srv_corr.columns = ["service", "abs_corr_with_satisfaction"]

st.dataframe(srv_corr)

st.info("💡 Returning customers show higher satisfaction rates compared to first-time customers. Thanks for more good factors and services.")

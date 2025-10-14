import streamlit as st
import pandas as pd
import plotly.express as px
from helper_functions import load_data

st.set_page_config(page_title="Overview", page_icon="📊", layout="wide")
st.title("📊 Overview — Airline Passenger Satisfaction")

df = load_data()

# Normalize satisfaction text

df["satisfaction"] = df["satisfaction"].astype(str).str.strip().str.lower()


total = len(df)
satisfied = (df["satisfaction"] == "satisfied").sum()
rate = satisfied / total * 100
st.metric("Overall satisfaction rate", f"{rate:.1f}%")

# Breakdown by Class

st.subheader("💺 Satisfaction by Class")
class_table = df.groupby("class")["satisfaction"].apply(
    lambda x: (x.eq("satisfied").sum() / len(x) * 100)
).reset_index().rename(columns={"satisfaction": "satisfied_percent"})
st.dataframe(class_table.round(2))
fig = px.bar(class_table, x="class", y="satisfied_percent",
            title="Satisfaction % by Travel Class",
            labels={"satisfied_percent": "% Satisfied"})
st.plotly_chart(fig, use_container_width=True)
    
st.info("💡 **Business** travelers are more satisfied by convenience, comfort, and entertainment.")


# Breakdown by Customer Type

st.subheader("🧳 Satisfaction by Customer Type")
cust_table = df.groupby("customer_type")["satisfaction"].apply(
    lambda x: (x.eq("satisfied").sum() / len(x) * 100)
).reset_index().rename(columns={"satisfaction": "satisfied_percent"})
st.dataframe(cust_table.round(2))
fig2 = px.bar(cust_table, x="customer_type", y="satisfied_percent",
            title="Satisfaction % by Customer Type",
            labels={"satisfied_percent": "% Satisfied"})
st.plotly_chart(fig2, use_container_width=True)
st.info("💡 **Returning** customers show higher satisfaction rates compared to first-time customers.")

st.markdown("---")
st.subheader("🧾 Data preview")
st.dataframe(df.head())

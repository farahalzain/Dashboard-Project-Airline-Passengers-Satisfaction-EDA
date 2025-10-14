import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from helper_functions import load_data

st.set_page_config(page_title="Operational Factors", page_icon="⚙️", layout="wide")
st.title("⚙️ Operational Factors — Airline Passenger Satisfaction")

# Load data
df = load_data()
df["satisfaction"] = df["satisfaction"].astype(str).str.strip().str.lower()

# Delays vs Satisfaction 
st.subheader("✈️ Delays vs Satisfaction")

# Create delay flag (1 = delayed, 0 = on time)
df["delayed"] = ((df["departure_delay"] > 15) | (df["arrival_delay"] > 15)).astype(int)

# Calculate satisfaction %
delay_summary = (
    df.groupby("delayed")["satisfaction"]
      .apply(lambda x: (x == "satisfied").mean() * 100)
    .reset_index(name="satisfied_percent")
)
delay_summary["delayed"] = delay_summary["delayed"].map({0: "No Delay", 1: "Delayed"})

# Seaborn plot
fig1, ax1 = plt.subplots(figsize=(6, 4))
sns.barplot(data=delay_summary, x="delayed", y="satisfied_percent", palette="Set2", ax=ax1)
ax1.set_title("Satisfaction by Delay Status")
ax1.set_xlabel("Delay Status")
ax1.set_ylabel("% Satisfied")
st.pyplot(fig1)

st.info("💡 Passengers with fewer delays report higher satisfaction levels.")

# Type of Travel vs Satisfaction 
st.markdown("---")
st.subheader("🧳 Type of Travel (Business vs Personal)")

travel_summary = (
    df.groupby("type_of_travel")["satisfaction"]
      .apply(lambda x: (x == "satisfied").mean() * 100)
    .reset_index(name="satisfied_percent")
)

fig2, ax2 = plt.subplots(figsize=(6, 4))
sns.barplot(data=travel_summary, x="type_of_travel", y="satisfied_percent", palette="pastel", ax=ax2)
ax2.set_title("Satisfaction by Type of Travel")
ax2.set_xlabel("Type of Travel")
ax2.set_ylabel("% Satisfied")
st.pyplot(fig2)

st.info("💡 Business travelers tend to be more satisfied than personal travelers.")

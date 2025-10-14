import streamlit as st
import pandas as pd
import plotly.express as px
from helper_functions import load_data

st.set_page_config(page_title="Demographics", page_icon="🧑‍🤝‍🧑", layout="wide")
st.title("🧑‍🤝‍🧑 Demographic Insights")

# Load data
df = load_data()

# Normalize satisfaction column
df["satisfaction"] = df["satisfaction"].astype(str).str.strip().str.lower()

# Age Group
st.subheader("👶➡️🧓 Satisfaction by Age Group")
bins = [0, 18, 30, 45, 60, 100]
labels = ["<18", "18-29", "30-44", "45-59", "60+"]
df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels, include_lowest=True)

age_table = (
    df.groupby("age_group")["satisfaction"]
      .apply(lambda x: (x == "satisfied").mean() * 100)
    .reset_index(name="satisfied_percent")
)

st.dataframe(age_table.round(2))

fig = px.bar(
    age_table,
    x="age_group",
    y="satisfied_percent",
    title="Satisfaction by Age Group",
    labels={"satisfied_percent": "% Satisfied", "age_group": "Age Group"},
    color="age_group"
)
st.plotly_chart(fig, use_container_width=True)
st.info("💡Passengers aged **45–59 years** report the **highest satisfaction** among all groups.")

# Gender 
st.subheader("🚹🚺 Satisfaction by Gender")

gender_table = (
    df.groupby("gender")["satisfaction"]
        .apply(lambda x: (x == "satisfied").mean() * 100)
    .reset_index(name="satisfied_percent")
)

st.dataframe(gender_table.round(2))

fig2 = px.bar(
    gender_table,
    x="gender",
    y="satisfied_percent",
    title="Satisfaction % by Gender",
    labels={"satisfied_percent": "% Satisfied", "gender": "Gender"},
    color="gender"
)
st.plotly_chart(fig2, use_container_width=True)
st.info("💡**Male passengers** show slightly higher satisfaction than females,  suggesting both genders are nearly equally satisfied.")

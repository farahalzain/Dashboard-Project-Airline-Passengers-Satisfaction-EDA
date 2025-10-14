import streamlit as st
from helper_functions import load_data

st.set_page_config(page_title="Conclusions", page_icon="🧩", layout="wide")
st.title("🧩 Conclusions & Recommendations")

df = load_data()

st.markdown("""
### Insights
- 💺 **Seat Comfort**, 🧼 **Cleanliness**, and 🛂 **Check-in Service** show strong positive influence on passenger satisfaction.
- ⏱️ **Departure/Arrival delays** reduce satisfaction notably; minimizing operational delays yields quick wins.
- 🤝 **Returning customers** tend to prioritize consistent in-flight service and comfort — investing here boosts retention.
- 🧑‍🤝‍🧑 **Passengers aged 45–59** report the highest satisfaction; males slightly more satisfied than females (≈2% difference).

### Overall Insights
- ✈️ **Business travelers** are generally more satisfied than personal travelers.
- 🏆 **Top drivers of satisfaction:** Online Boarding, In-Flight Entertainment.
- ⚖️ **Moderate drivers:** Seat Comfort, On Board Service, Leg_room Service, Cleanliness.
- 📉 **Lesser (but still important) drivers:** In-Flight Wifi Service, In-Flight Service, Check In Service, Baggage Handling, Ease Online Booking, Food & Drink.

### Recommendations for Airlines
1. Prioritize improvements in seat comfort, cabin cleanliness, and check-in experience.  
2. Reduce delays and communicate proactively when they occur.  
3. Target loyalty programs improving services that matter most for returning customers.  
4. Segment feedback by **age, class, travel type** to personalize services and promotions.
""")

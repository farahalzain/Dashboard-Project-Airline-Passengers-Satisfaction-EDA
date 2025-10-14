import streamlit as st
st.set_page_config(page_title= "Airline Satisfaction Dashboard", page_icon="✈️", layout="wide")
st.title("✈️ Airline Passenger Satisfaction Dashboard")
st.subheader("Explore passenger satisfaction drivers and operational insights")

col1, col2 = st.columns([1,4])
with col1:
    st.write("This dashboard analyzes airline passenger feedback to reveal which services, demographics and operational factors drive satisfaction.")
with col2:
    st.image("airline_logo.jpg", width=250)
    
st.markdown("""
### 🧭 Navigate between pages:
- **Overview**: overall satisfaction rate, breakdown by Class & Customer Type.  
- **Service Impact**: correlation heatmap and service drivers.  
- **Operational Factors**: delays & type of travel analysis.  
- **Demographics**: age groups & gender analysis.  
- **Customer Loyalty**: Loyal vs Disloyal customer analysis.  
- **Conclusions**: executive summary & recommendations.
""")
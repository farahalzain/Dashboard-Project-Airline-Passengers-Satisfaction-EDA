# Dashboard-Project-Airline-Passengers-Satisfaction-EDA
# ✈️ Airline Passenger Satisfaction Dashboard

## 📊 Overview
This interactive **Streamlit dashboard** analyzes the **Airline Passenger Satisfaction dataset** to help airlines understand what drives passenger satisfaction, optimize services, and enhance loyalty programs.  

The dashboard covers **operational, demographic, and service-related factors**, with interactive charts and tables.

---

## 📂 Dataset
- **Source:** Kaggle — Airline Passenger Satisfaction  
- **Records:** Each row represents a passenger survey  
- **Key Features:**
  - `Passenger ID`, `Gender`, `Age`
  - `Customer Type` (Loyal / Disloyal)
  - `Type of Travel` (Business / Personal)
  - `Class` (Economy, Business, First)
  - `Flight Distance`, `Departure Delay`, `Arrival Delay`
  - Service ratings (1–5): `Seat Comfort`, `In-flight Entertainment`, `Wi-Fi`, etc.
  - `Satisfaction` (Satisfied / Neutral or Dissatisfied)

---

## 🗂️ Project Structure

```

AirlinePassengerSatisfactionDashboard/
│
├── Home.py                         # Main page (project introduction)
├── pages
    ├── Overview.py                 # Overall satisfaction and breakdown by class and customer type
    ├── Service Impact.py           # Which services drive satisfaction
    ├── Operational Factors.py      # Effect of delays and travel type on satisfaction
    ├── Demographics Insights.py             # Satisfaction by age group and gender
    ├── Customer Loyalty.py         # Loyal vs Disloyal satisfaction and service correlations
    ├──Conclusions.py               # Executive summary and recommendations.py                 
    
├── helper_function.py              # Data loading helper
├── requirements.txt                # required libraries
├── airline_logo.jpg                # photo 
└── airline_satisfaction.csv        # Dataset

````
---

## 🧭 Dashboard Pages

### 🌍 Overview
- **Overall satisfaction rate** (percentage of satisfied passengers)
- **Breakdown by Class** (Economy, Business, First) ✈️
- **Breakdown by Customer Type** (Loyal vs Disloyal) 🤝
- **Data preview** 📝

### 🔗 Service Impact
- Correlation heatmap: **Which services drive satisfaction the most?**  
- Identify **top, moderate, and lesser drivers** of satisfaction

### ⚙️ Operational Factors
- **Delays vs Satisfaction** ⏱️
- **Type of Travel** (Business vs Personal) 🧳

### 🧑‍🤝‍🧑 Demographics
- Satisfaction by **Age Group** 👶🧓
- Satisfaction by **Gender** 👨👩

### 🤝 Customer Loyalty
- **Loyal vs Disloyal** satisfaction
- **Top services affecting loyal passengers**

### 🧩 Conclusions
- Executive summary with **key drivers** and **recommendations**  
- Includes business insights and actionable suggestions


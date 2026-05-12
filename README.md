# ✈️ Airline Passenger Satisfaction Analysis & Dashboard

## 📊 Project Overview

In the competitive airline industry, passenger satisfaction plays a major role in customer loyalty, repeat business, and overall brand reputation.

This project combines **Exploratory Data Analysis (EDA)** and an **interactive Streamlit dashboard** to analyze airline passenger feedback data and uncover insights that help improve customer experience and airline services.

The project focuses on identifying the key factors affecting passenger satisfaction, including service quality, delays, travel class, demographics, and customer loyalty.

---

# 🎯 Objectives

* Analyze passenger satisfaction patterns across different customer groups
* Identify the strongest drivers of satisfaction
* Explore the impact of delays and operational factors
* Compare satisfaction across travel classes and demographics
* Build an interactive dashboard for data exploration
* Provide actionable business recommendations for airlines

---

# 🛠️ Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit
* Jupyter Notebook

---

# 📂 Dataset

**Source:** Kaggle — Airline Passenger Satisfaction Dataset

### Dataset Information

* Rows: 129,880
* Columns: 24

### Key Features

* Passenger demographics
* Customer Type (Loyal / Disloyal)
* Travel Class
* Flight Distance
* Departure & Arrival Delays
* Service Ratings
* Satisfaction Status

---

# 🧹 Data Cleaning & Preprocessing

The following preprocessing steps were performed:

* Removed duplicates
* Handled missing values
* Standardized column names
* Treated outliers in delay columns
* Prepared categorical and numerical variables for analysis

---

# 📈 Exploratory Data Analysis (EDA)

The analysis explored:

* Passenger satisfaction across travel classes
* Loyal vs disloyal customer behavior
* Impact of delays on customer experience
* Service quality ratings and correlations
* Demographic trends by age and gender
* Flight distance and satisfaction relationship

---

# 🔍 Key Insights

## ✈️ Travel Class

* Business Class passengers showed the highest satisfaction levels.
* Economy and Economy Plus require service improvements.

## 🤝 Customer Loyalty

* Returning customers were significantly more satisfied than first-time passengers.
* Online boarding, entertainment, and seat comfort strongly influenced loyalty.

## 🌐 Service Drivers

Top satisfaction drivers:

* Online boarding
* In-flight Wi-Fi
* Seat comfort
* Entertainment
* Cleanliness

Moderate drivers:

* Check-in service
* Baggage handling
* On-board service

## ⏱️ Delays

* Flight delays negatively impacted satisfaction.
* Even small delay reductions improved customer experience.

## 🧑 Demographics

* Younger passengers showed lower satisfaction levels.
* Satisfaction differences were more related to age than gender.

---

# 📊 Interactive Dashboard (Streamlit)

The project includes a multi-page interactive Streamlit dashboard.

## Dashboard Pages

### 🌍 Overview

* Overall satisfaction rate
* Satisfaction by class
* Satisfaction by customer type
* Dataset preview

### 🔗 Service Impact

* Correlation heatmap
* Service importance analysis

### ⚙️ Operational Factors

* Delays vs satisfaction
* Travel type analysis

### 🧑‍🤝‍🧑 Demographics Insights

* Satisfaction by age group
* Satisfaction by gender

### 🤝 Customer Loyalty

* Loyal vs disloyal customers
* Key loyalty drivers

### 🧩 Conclusions

* Executive summary
* Recommendations and business insights

---

# 💡 Recommendations

* Improve Economy & Economy Plus services
* Enhance first-time passenger experience
* Optimize online services and boarding process
* Reduce delays and improve communication
* Build targeted loyalty programs
* Improve digital experience for younger passengers

---

# 🗂️ Project Structure

```bash
AirlinePassengerSatisfactionDashboard/
│
├── Airline_Passenger_Satisfaction.ipynb/
├── dashboard/
├── pages/ 
  ├── Conclusion.py  
  ├── Customer Loyalty.py  
  ├── Demographic Insights.py  
  ├── Operational Factors.py  
  ├── Overview.py
  └── Service Impact.py
├── Home.py
├── helper_function.py
├── requirements.txt
├── README.md
└── airline_satisfaction.csv
```

---

# 🚀 Skills Demonstrated

* Exploratory Data Analysis
* Data Cleaning
* Dashboard Development
* Streamlit Application Development
* Data Visualization
* Business Insight Extraction
* Customer Behavior Analysis

---

import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path=r"D:\farah\bootcamp\AirlinePassengerSatisfactionDashboard\airline_passenger_satisfaction.csv"):
    df = pd.read_csv(path)
    # normalize column names
    df.columns = df.columns.str.strip().str.replace(r"[ -]", "_", regex=True).str.lower()
    # df = df.rename(columns={ "check-in_service":"checkin_service"})
    
    # drop ID columns 
    df = df.drop(columns="id")    

    # Convert numeric columns
    num_cols = [
        "age", "flight_distance", "departure_delay", "arrival_delay",
        "ease_of_online_booking", "check_in_service", "in_flight_service",
        "seat_comfort", "in_flight_entertainment", "food_and_drink",
        "in_flight_wifi_service", "cleanliness", "baggage_handling"
    ]
    for c in num_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    # Standardize satisfaction labels if present
    df["satisfaction"] = df["satisfaction"].astype(str).str.strip()

    # Fill small number of numeric NaNs with column medians (simple, safe)
    for c in num_cols:
        df[c] = df[c].fillna(df[c].median())

    for c in df.select_dtypes(include="object").columns:
        df[c] = df[c].fillna("Unknown")

    return df

# ID,Gender,Age,Customer Type,Type of Travel,Class,Flight Distance,Departure Delay,Arrival Delay,Departure and Arrival Time Convenience,Ease of Online Booking,Check-in Service,Online Boarding,Gate Location,On-board Service,Seat Comfort,Leg Room Service,Cleanliness,Food and Drink,In-flight Service,In-flight Wifi Service,In-flight Entertainment,Baggage Handling,Satisfaction
data = load_data()
print(data.columns.tolist)
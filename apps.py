import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline/model
model = joblib.load("./models/random_forest.pkl")

st.set_page_config(page_title="California House Price Prediction")

st.title("🏡 California House Price Prediction")

st.write("Enter the property details below:")

# Input fields
longitude = st.number_input("Longitude", value=-122.23, format="%.4f")
latitude = st.number_input("Latitude", value=37.88, format="%.4f")
housing_median_age = st.number_input("Housing Median Age", min_value=1, value=41)

total_rooms = st.number_input("Total Rooms", min_value=1, value=2500)
total_bedrooms = st.number_input("Total Bedrooms", min_value=1, value=500)
population = st.number_input("Population", min_value=1, value=1200)
households = st.number_input("Households", min_value=1, value=450)
median_income = st.number_input("Median Income", min_value=0.0, value=3.5,format="%.4f")

if st.button("Predict House Price"):
    room_per_house=total_rooms/households
    bedroom_per_house=total_bedrooms/households
    beds_per_room=total_bedrooms/total_rooms

    input_df = pd.DataFrame({
        "longitude": [longitude],
        "latitude": [latitude],
        "housing_median_age": [housing_median_age],
        "room_per_house": [room_per_house],
        "total_rooms": [total_rooms],
        "beds_per_room": [beds_per_room],
        "total_bedrooms": [total_bedrooms],
        "bedroom_per_house": [bedroom_per_house],
        "population": [population],
        "households": [households],
        "median_income": [median_income]
    })

    prediction = model.predict(input_df)

    st.success(f"🏠 Estimated House Value: ${prediction[0]:,.2f}")
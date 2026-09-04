import joblib
import pandas as pd
import streamlit as st

pipeline=joblib.load("car_price_prediction.pkl")

st.title("Used car price prediction")
Brand=st.text_input("Enter Brand")
Vehicle_age=st.number_input(
    "vehicle age",
    min_value=0,
    max_value=30,
    value=5,
)
km_driven=st.number_input(
    "kilometers Driven",
    min_value=0,
    value=30000
)
fuel_type=st.selectbox(
    "fuel_type",["petrol","Desiel","CNG","LPG","Electric"]
)
seller_type=st.selectbox(
    "seller type",
    ["Dealer","Individual"]
)
transmission=st.selectbox(
    "Transmission",
    ["manual","Automatic"]
)
Mileage=st.number_input(
    "mileage",
    min_value=0.0,
    value=20.0
)
max_power=st.number_input(
    "max Power(BHP)",
    min_value=0.0,
    max_value=10,
    value=5
)
year=st.number_input(
    "year of Purchase",
    min_value=2000,
    max_value=2026,
    value=2018
)
Present_price=st.number_input(
    "present  Price (lakhs)",
    min_values=0.0,
    value=5.0
)
owner=st.number_input(
    "previous owners",
    min_value=0,
    max_value=5,
    value=0
)
seats=st.number_input(
    "number od seats",
    min_value=0,
    max_value=10,
    value=5,
)
if st.button("Predict price"):
    input_data=pd.DataFrame({
        "year":[year],
        "Present_price":[Present_price],
        "fuel_type":[fuel_type],
        "seller_type":[seller_type],
        "transmission":[transmission],
        "owner":[owner],
        "max_power":[max_power],
        "Mileage":[Mileage],
        "km_driven":[km_driven],
        "seats":[seats]
    })
    prediction =pipeline.predict(input_data)
    st.success(f"Prediction Selling Price:₹{prediction[0]:,2f}Lakhs")
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('linear_model.pkl')

st.title("🏠 Bangalore House Price Prediction")

# User inputs
area_type = st.selectbox("Area Type", ["Super built-up  Area", "Built-up  Area", "Plot  Area", "Carpet  Area"])
location = st.text_input("Location", "Whitefield")
total_sqft = st.number_input("Total Area (sq ft)", value=1200)
bath = st.number_input("Number of Bathrooms", min_value=1, max_value=20, value=2)
balcony = st.number_input("Number of Balconies", min_value=0, max_value=20, value=1)
bhk = st.number_input("Number of BHK", min_value=1, max_value=200, value=2)

# Predict
if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        'total_sqft': total_sqft,
        'bath': bath,
        'balcony': balcony,
        'BHK': bhk,
        'area_type': area_type,
        'location': location
    }])

    price = model.predict(input_df)[0]
    st.success(f"💰 Estimated House Price: ₹{price:.2f} Lakhs")

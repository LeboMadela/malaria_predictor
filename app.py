# app.py

import streamlit as st
import pandas as pd
import joblib

# Load your trained model
model = joblib.load("malaria_case_predictor_model.pkl")

# Title and description
st.title("Malaria Case Predictor (Africa)")
st.markdown("This tool predicts estimated malaria cases using health-related data. Built for SDG 3: Good Health and Well-being.")

# Input fields for user
st.subheader("Enter Health Data:")

year = st.slider("Year", min_value=2010, max_value=2025, value=2017)
deaths_median = st.number_input("No. of Deaths (Median)", min_value=0, value=5000)
deaths_min = st.number_input("No. of Deaths (Min)", min_value=0, value=4500)
deaths_max = st.number_input("No. of Deaths (Max)", min_value=0, value=5500)
cases_reported = st.number_input("Reported Malaria Cases", min_value=0, value=1500000)
deaths_reported = st.number_input("Reported Malaria Deaths", min_value=0, value=3000)
incidence = st.number_input("Malaria Incidence per 1000 at-risk population", min_value=0.0, value=200.0)

# Predict button
if st.button("Predict Malaria Cases"):
    input_data = pd.DataFrame([[
        year,
        deaths_median,
        deaths_min,
        deaths_max,
        cases_reported,
        deaths_reported,
        incidence
    ]], columns=[
        'Year',
        'No. of deaths_median',
        'No. of deaths_min',
        'No. of deaths_max',
        'No. of cases_reported',
        'No. of deaths_reported',
        'No. of cases'
    ])

    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Malaria Cases: **{int(prediction):,}**")

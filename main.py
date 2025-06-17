import streamlit as st
import pandas as pd 
import joblib
import sklearn
print(sklearn.__version__)

# --- Load pre-trained model ---
@st.cache_resource
def load_model():
    return joblib.load("carbon_model.pkl")

model = load_model()

# --- Streamlit UI ---
st.title("🌍 Weekly Carbon Footprint Estimator")

diet = st.selectbox("What is your diet?", ["omnivore", "vegetarian", "vegan", "pescatarian"])
transport = st.selectbox("Primary mode of transport?", ["private", "public", "walk/bicycle"])
heating = st.selectbox("Heating energy source?", ["electric", "coal", "natural gas", "wood"])
vehicle_km = st.number_input("Vehicle distance per month (km)", min_value=0, value=100)
tv_hours = st.slider("Daily hours watching TV/PC", 0, 24, 4)
internet_hours = st.slider("Daily hours using the internet", 0, 24, 5)
efficiency = st.selectbox("Home energy efficiency?", ["Yes", "No", "Sometimes"])

# Predict
if st.button("Estimate My CO₂ Emission"):
    input_data = pd.DataFrame([{
        "Diet": diet,
        "Transport": transport,
        "Heating Energy Source": heating,
        "Vehicle Monthly Distance Km": vehicle_km,
        "How Long TV PC Daily Hour": tv_hours,
        "How Long Internet Daily Hour": internet_hours,
        "Energy efficiency": efficiency
    }])
    
    prediction = model.predict(input_data)[0]
    st.success(f"🌱 Estimated Weekly CO₂ Emission: **{prediction:.2f} kg**")

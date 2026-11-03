import streamlit as st
import pickle
import pandas as pd

# Page setup
st.set_page_config(page_title="Titanic Survival Prediction")
st.title("🚢 Titanic Survival Prediction")
st.write("Enter passenger details to predict survival!")

# Load model
with open('titanic_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Inputs
pclass = st.selectbox("Ticket Class", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 100, 25)
sibsp = st.number_input("Siblings/Spouses", 0, 10, 0)
parch = st.number_input("Parents/Children", 0, 10, 0)
fare = st.number_input("Fare", 0.0, 600.0, 50.0)

# Predict button
if st.button("Predict Survival"):
    sex_num = 0 if sex == "male" else 1
    input_data = [[pclass, sex_num, age, sibsp, parch, fare]]
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.success("✅ SURVIVED! This passenger would have survived!")
    else:
        st.error("❌ NOT SURVIVED! This passenger would not have survived.")
    st.balloons()

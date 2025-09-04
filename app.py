# app.py
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('Laptop_price_model.pkl')

# Load the training columns
training_columns = joblib.load("model_columns.pkl")

st.title("Laptop Price Predictor")
st.write('Enter laptop features to predict the price:')

# User Inputs
company = st.selectbox('Company', ['HP', 'Dell', 'MacOS', 'Lenovo', 'Asus'])
ram = st.selectbox('RAM (GB)', [2,4, 8, 12,16])
opsys = st.selectbox('Operating System', ['Windows', 'MacOS', 'Linux', 'Other'])
typename = st.selectbox('Laptop Type',['Workstations','Gaming','Ultrabooks','Notebooks','Netbooks'])

# Convert input into a DataFrame
user_input = pd.DataFrame({'Company': [company],'Ram': [ram],'OpSys': [opsys],'TypeName' : [typename]})

# Encoding (simplest approach) 
user_input_encoded = pd.get_dummies(user_input)

# Ensure same columns as training 
for col in training_columns:
    if col not in user_input_encoded:
        user_input_encoded[col] = 0

# Reorder columns
user_input_encoded = user_input_encoded[training_columns]

# Predict and display 
if st.button('Predict Price'):
    prediction = model.predict(user_input_encoded)
    st.success(f'Predicted Laptop Price: {Price_euros[0]:.2f}')


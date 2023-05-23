import streamlit as st

st.title("My first Streamlit App")

weight = st.number_input('Insert your weight')
age = st.number_input('Insert your age')
height = st.number_input('Insert your height')

import pandas as pd
user_input = pd.DataFrame([[weight, age, height]], columns=['weight', 'age', 'height'])

import joblib

model = joblib.load('model.pkl')

prediction = model.predict(user_input)

if st.button('Predict'):
   st.write(prediction[0])
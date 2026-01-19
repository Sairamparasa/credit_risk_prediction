import streamlit as st
import pandas as pd
import numpy as np
import joblib 
import os

# Get the directory of the current script and build paths relative to project root
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
models_dir = os.path.join(project_root, 'models')

model = joblib.load(os.path.join(models_dir, 'random_forest_credit_model.pkl'))
encoders = {col: joblib.load(os.path.join(models_dir, f"{col}_encoder.pkl")) 
           for col in ['Sex','Housing','saving_accounts','checking_account']}

st.title("Credit Risk Prediction App")
st.write('Enter application information to predict if the credit risk is good or bad')

age = st.number_input("Age" , min_value=18,max_value=80,value=30)
sex = st.selectbox("Sex",['male','female'])
job = st.number_input('Job',min_value=0,max_value=3,value=1)
housing = st.selectbox('Housing',['own', 'free', 'rent'])
saving_accounts = st.selectbox('Saving accounts',['little', 'moderate', 'quite rich', 'rich'])
checking_account = st.selectbox('Checking account',['moderate', 'little', 'rich'])
credit_amount = st.number_input('Credit amount',min_value=0,value=1000)
duration = st.number_input('Duration (months)',min_value=1,max_value=30,value=12)

input_df = pd.DataFrame({
    'Age':[age],
    'Sex':[encoders['Sex'].transform([sex])[0]],
    'Job':[job],
    'Housing' : [encoders['Housing'].transform([housing])[0]],
    'Saving accounts':[encoders['saving_accounts'].transform([saving_accounts])[0]],
    'Checking account':[encoders['checking_account'].transform([checking_account])[0]],
    'Credit amount':[credit_amount],
    'Duration':[duration]
    }) 

if st.button("Predict Risk"):
    pred = model.predict(input_df)[0]

    if pred == 1:
        st.success('The Predicted Credit is: **Good**')
    else:
        st.success('The Predicted Credit is: **Bad**')
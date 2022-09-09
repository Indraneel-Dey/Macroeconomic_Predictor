import streamlit as st
import pickle
import numpy as np
from sklearn.linear_model import RidgeCV

gdp = pickle.load(open('gdp.pkl', 'rb'))

st.write('Indraneel Dey')
st.write('Indian Institute of Technology, Madras')
st.title('Macroeconomics Predictor')
st.text('Input the values of macroeconomic statistics of India below and get the prediction')
st.text('of GDP of that year')
st.write("Enter the Population in billions")
pop = st.number_input('Population', min_value=0.5)
st.write("Enter the Unemployment rate in percentage")
ur = st.number_input('Unemployment Rate', min_value=0.0)
st.write("Enter the annual Per Capita Income in USD")
pci = st.number_input('Per Capita Income', min_value=500.0)
st.write("Enter the Exchange Rate of Rupee vs USD, i.e, 1 USD in INR")
er = st.number_input('Exchange Rate', min_value=50.0)
st.write("Enter the annual Trade Balance (Exports - Imports) in billion USD")
tb = st.number_input('Trade Balance', min_value=0.0)
st.write("Enter the Foreign Exchange Reserves in billion USD")
ir = st.number_input('Foreign Exchange Reserves', min_value=100.0)
st.write("Enter the annual Rainfall in mm")
rainfall = st.number_input('Rainfall', min_value=500.0)
st.write("Enter the Inflation rate in percentage")
inflation = st.number_input('Inflation Rate', min_value=0.0)
st.write("Enter the RBI Policy Interest rate in percentage")
pir = st.number_input('Policy Interest Rate', min_value=3.0)
st.write("Enter the Current Account Deficit in percentage of GDP")
deficit = st.number_input('Current Account Deficit', min_value=-10.0)
st.write("Enter the Public Debt in percentage of GDP")
debt = st.number_input('Public Debt', min_value=0.0)
st.write("Enter the Tax in percentage of GDP")
tax = st.number_input('Tax', min_value=5.0)
st.write("The GDP in billion USD is predicted below")
st.write("GDP of 2020: 2667.69 billion USD")

x = np.array([[pop, ur, pci, er, tb, ir, rainfall, inflation, pir, deficit, debt, tax]])
gdp_predict = gdp.predict(x)

if st.button('Predict'):
    st.header('GDP')
    st.text(gdp_predict[0])

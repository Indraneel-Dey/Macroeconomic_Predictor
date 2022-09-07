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
st.write("Enter the Population in billions. For example if you want to input 1 billion, enter '1'")
pop = float(st.text_input('Population', '1.38'))
st.write("Enter the Unemployment rate in percentage. For example if you want to input 3%, enter '3'")
ur = float(st.text_input('Unemployment Rate', '8'))
st.write("Enter the annual Per Capita Income in US $. For example if you want to input 1000 USD, enter '1000'")
pci = float(st.text_input('Per Capita Income', '1817.82'))
st.write("Enter the Exchange Rate of Rupee vs USD. For example if you want to input 1 USD = 75 Rupees, enter '75'")
er = float(st.text_input('Exchange Rate', '72.971'))
st.write("Enter the annual Trade Balance (Exports - Imports) in billion USD. For example if you want to input excess import of 100 billion USD, enter '-100'")
tb = float(st.text_input('Trade Balance', '-96.55'))
st.write("Enter the Foreign Exchange Reserves in billion USD. For example if you want to input 400 billion USD of Foreign Exchange Reserves for India, enter '400'")
ir = float(st.text_input('Foreign Exchange Reserves', '477.81'))
st.write("Enter the annual Rainfall in mm. For example if you want to input 1000 mm rainfall in India, enter '1000'")
rainfall = float(st.text_input('Rainfall', '1116.4'))
st.write("Enter the Inflation rate in percentage. For example if you want to input inflation of 5%, enter '5'")
inflation = float(st.text_input('Inflation Rate', '6.18'))
st.write("Enter the RBI Policy Interest rate in percentage. For example if you want to input 6%, enter '6'")
pir = float(st.text_input('Policy Interest Rate', '4'))
st.write("Enter the Current Account Deficit in percentage of GDP. For example if you want to input deficit of 4% of GDP, enter '4'")
deficit = float(st.text_input('Current Account Deficit', '9.4'))
st.write("Enter the Public Debt in percentage of GDP. For example if you want to input debt of 65% of GDP, enter '65'")
debt = float(st.text_input('Public Debt', '73.95'))
st.write("Enter the Tax in percentage of GDP. For example if you want to input 10%, enter '10'")
tax = float(st.text_input('Tax', '10.9'))
st.write("The GDP in billion USD is predicted below")
st.write("GDP of 2020: 2667.69 billion USD")

x = np.array([[pop, ur, pci, er, tb, ir, rainfall, inflation, pir, deficit, debt, tax]])
gdp_predict = gdp.predict(x)

if st.button('Predict'):
    st.header('GDP')
    st.text(gdp_predict[0])

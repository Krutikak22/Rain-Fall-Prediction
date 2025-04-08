import streamlit as st
import joblib
import sklearn

mymodel = joblib.load('model.pkl')

st.title("Rainfall Prediction")

a1 = st.number_input("Enter Pressure : ")
a2 = st.number_input("Enter Dewpoint : ")
a3 = st.number_input("Enter Humidity : ")
a4 = st.number_input("Enter Cloud : ")
a5 = st.number_input("Enter Sunshine : ")
a6 = st.number_input("Enter Winddirection : ")
a7 = st.number_input("Enter Windspeed : ")

if st.button("Project"):
    op = mymodel.predict([[a1, a2, a3, a4, a5, a6, a7]])
    if op == 1:
        st.write('Barish Hogi!!!')
    else:
        st.write('Barish Nahi Hogi!!!')

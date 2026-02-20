import streamlit as st
st.sidebar.title("bmi calculator")
st.sidebar.subheader("navigation")
st.title("bmi calculator app")
h=st.number_input("enter your height in cm")
w=st.number_input("enteer your weight in kg")
if st.button("calculator bmi"):
    bmi=w(h/100)**2
    st.success(f"your bmi is {bmi:.2f}")
"""app.py"""

import streamlit as st

def add(a, b):
    return a+b

st.title("Simple Addition App")

a = st.number_input("Enter first number", 0, 100)
b = st.number_input("Enter second number", 0, 100)

if st.button("Add"):
    result = add(a, b)
    st.markdown(f"The result is {result}")
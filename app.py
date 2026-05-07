import streamlit as st
import numpy as np
st.title("🏠House Price Predictor AI")
st.write("Enter the house details below to get an estimated valuation.")

rooms=st.number_input("Number of Rooms",min_value=1,max_value=10,value=3)
sqft=st.number_input("Total Square Feet Area",min_value=300,max_value=10000,value=1500)


if st.button("Predict House Price"):
   base_price=(rooms*25000)+(sqft*150)
   st.success(f"Estimated Valuation:${base_price:,.2f}")
  


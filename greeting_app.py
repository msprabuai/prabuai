import streamlit as st
from datetime import date, timedelta

# Page config
st.set_page_config(page_title="Simple Greeting App", page_icon="👋")

st.title("👋 Greeting App")

# Input fields
name = st.text_input("Enter your name:")
age = st.slider("Select your age:", min_value=1, max_value=120, value=25)

# Button
if st.button("Generate Greeting"):
    if name.strip():

        # Calculate days lived based on current date
        today = date.today()
        days_lived = age * 365  # Basic calculation (ignoring leap years)

        # Greeting message
        greeting = f"Hello {name}! You are {age} years old."

        st.success(greeting)
        
        st.metric("Estimated Days Lived", f"{days_lived:,}")

    else:
        st.error("Please enter your name before submitting.")

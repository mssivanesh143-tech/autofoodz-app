import streamlit as st

st.title("Hello AUTOFOODZ!")
st.write("My first Streamlit app 🎉")



st.title("🍕 AUTOFOODZ - Web Frontend Workflow")

st.header("Step 1: Environment Setup")
st.success("✅ Streamlit installed successfully!")

st.header("Step 2: UI Components")
name = st.text_input("Enter your name:")
btn = st.button("Submit")

if btn:
    st.write(f"Hello, {name}! Welcome to AUTOFOODZ 🎉")

st.header("Step 3: State Management")
count = st.slider("Select order quantity:", 0, 10)
st.write(f"You ordered: {count} items")
         

import pandas as pd

st.title("🍕 AUTOFOODZ - Food Order System")

# --- Step 2: UI Components ---
st.header("📋 Place Your Order")

name = st.text_input("Your Name:")
food = st.selectbox("Choose Food:", ["Biryani", "Dosa", "Pizza", "Burger", "Idli"])
qty = st.slider("Quantity:", 1, 10)

# --- Step 3: State Management ---
prices = {"Biryani": 150, "Dosa": 50, "Pizza": 200, "Burger": 120, "Idli": 40}

# --- Step 4: Logic Implementation ---
if st.button("Place Order"):
    total = prices[food] * qty
    st.success(f"✅ Order placed for {name}!")
    st.info(f"🍽️ {qty} x {food} = ₹{total}")

    # Store order in table
    data = {"Item": [food], "Qty": [qty], "Price Each": [f"₹{prices[food]}"], "Total": [f"₹{total}"]}
    df = pd.DataFrame(data)
    st.table(df)

# --- Sidebar ---
st.sidebar.title("AUTOFOODZ 🍴")
st.sidebar.write("Internship Project")
st.sidebar.write(f"Student: Sivanesh M")


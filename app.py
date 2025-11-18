import streamlit as st

st.title("🧮 Simple Calculator")

# Inputs
num1 = st.number_input("Enter first number:", format="%.2f")
num2 = st.number_input("Enter second number:", format="%.2f")

# Operation selection
operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculate button
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {result}")

    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {result}")

    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {result}")

    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {result}")
        else:
            st.error("Error: Division by zero is not allowed!")

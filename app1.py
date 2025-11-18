import streamlit as st
from datetime import date, datetime

st.title("🧮 Age Calculator")

st.write("Enter your date of birth to calculate your current age.")

# Input: Date of Birth
dob = st.date_input("Select your Date of Birth")

# Button to calculate age
if st.button("Calculate Age"):
    today = date.today()

    if dob > today:
        st.error("Date of birth cannot be in the future!")
    else:
        # Calculate years
        years = today.year - dob.year
        
        # Adjust if birthday hasn't happened yet in current year
        if (today.month, today.day) < (dob.month, dob.day):
            years -= 1

        # Calculate months and days
        last_birthday = dob.replace(year=today.year)
        if last_birthday > today:
            last_birthday = dob.replace(year=today.year - 1)

        delta = today - last_birthday
        months = delta.days // 30
        days = delta.days % 30

        st.success(f"🎉 Your Age: **{years} years, {months} months, {days} days**")

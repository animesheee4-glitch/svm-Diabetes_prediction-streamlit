import streamlit as st
from datetime import date

st.set_page_config(page_title="Age Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Fun Age Calculator")

# Input: Date of Birth
dob = st.date_input("📅 Select your Date of Birth", min_value=date(1900,1,1))

# Button to calculate age
if st.button("Calculate Age"):
    today = date.today()

    if dob > today:
        st.error("❌ Date of birth cannot be in the future!")
    else:
        # Calculate years
        years = today.year - dob.year
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

        # ✅ Congratulate if above 18
        if years >= 18:
            st.balloons()
            st.success("👏 Congratulations! You are officially an adult 🎉")
        else:
            st.info("🌱 You’re still under 18 — enjoy your youth!")

        # 🎂 Next birthday countdown
        next_birthday = dob.replace(year=today.year)
        if next_birthday < today:
            next_birthday = dob.replace(year=today.year + 1)
        days_to_birthday = (next_birthday - today).days
        st.info(f"🎂 Your next birthday is in **{days_to_birthday} days**!")

        # 🔮 Zodiac sign
        def zodiac_sign(dob):
            m, d = dob.month, dob.day
            if (m==3 and d>=21) or (m==4 and d<=19): return "Aries 🐏"
            if (m==4 and d>=20) or (m==5 and d<=20): return "Taurus 🐂"
            if (m==5 and d>=21) or (m==6 and d<=20): return "Gemini 👯"
            if (m==6 and d>=21) or (m==7 and d<=22): return "Cancer 🦀"
            if (m==7 and d>=23) or (m==8 and d<=22): return "Leo 🦁"
            if (m==8 and d>=23) or (m==9 and d<=22): return "Virgo 🌾"
            if (m==9 and d>=23) or (m==10 and d<=22): return "Libra ⚖️"
            if (m==10 and d>=23) or (m==11 and d<=21): return "Scorpio 🦂"
            if (m==11 and d>=22) or (m==12 and d<=21): return "Sagittarius 🏹"
            if (m==12 and d>=22) or (m==1 and d<=19): return "Capricorn 🐐"
            if (m==1 and d>=20) or (m==2 and d<=18): return "Aquarius 🏺"
            if (m==2 and d>=19) or (m==3 and d<=20): return "Pisces 🐟"
        st.write(f"🔮 Your Zodiac Sign: **{zodiac_sign(dob)}**")

        # 😂 Funny life units
        days_lived = (today - dob).days
        chapatis = days_lived * 3
        sleep_hours = days_lived * 8
        heartbeats = days_lived * 24 * 60 * 72  # average 72 bpm
        st.write(f"🗓️ You’ve lived **{days_lived} days**")
        st.write(f"😴 That’s about **{sleep_hours} hours of sleep** (assuming 8 hrs/day)")
        st.write(f"🍽️ And probably eaten ~**{chapatis} chapatis** 😂")
        st.write(f"❤️ Your heart has beaten ~**{heartbeats:,} times** already!")

        # 📊 Life expectancy progress bar
        life_expectancy = 72
        progress = min(years / life_expectancy, 1.0)
        st.progress(progress)
        st.caption(f"📊 You’ve lived {(progress*100):.2f}% of the average lifespan!")

        # 🎉 Birthday surprise
        if today.month == dob.month and today.day == dob.day:
            st.balloons()
            st.snow()
            st.success("🎉 Happy Birthday! Don’t forget to share cake 🍰") 
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Growth Mindset Project", page_icon="🧠", layout="wide")

# Custom CSS for Styling
def apply_custom_styles():
    st.markdown(
        """
        <style>
            body {
                background-color: #1e1e2f;
                color: white;
                font-family: Arial, sans-serif;
            }
            .title {
                color: #f39c12;
                text-align: center;
                font-size: 36px;
            }
            .header {
                color: #e74c3c;
                font-size: 24px;
            }
            .text-box {
                background-color: #2c3e50;
                padding: 10px;
                border-radius: 10px;
            }
            .footer {
                text-align: center;
                font-size: 18px;
                color: #95a5a6;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

apply_custom_styles()

# App Title
st.markdown("<h1 class='title'>Growth Mindset Challenge</h1>", unsafe_allow_html=True)

# Introduction
st.markdown("<h2 class='header'>🚀 Welcome to Your Growth Journey!</h2>", unsafe_allow_html=True)
st.write("Develop a strong growth mindset with this interactive app. Track your progress, reflect on challenges, and celebrate achievements. Let's start! 💪")

# Quote Section
st.markdown("<h2 class='header'>💡 Daily Growth Mindset Quote</h2>", unsafe_allow_html=True)
st.markdown("<div class='text-box'>🌟 'Success is not final, failure is not fatal: It is the courage to continue that counts.' - Winston Churchill</div>", unsafe_allow_html=True)

# Growth Mindset Goal Input
st.markdown("<h2 class='header'>🎯 Set Your Goal for Today</h2>", unsafe_allow_html=True)
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"Great! You're working on: {user_input}. Keep moving forward! 🚀")
else:
    st.warning("Write about a challenge you're facing today to gain clarity and focus.")

# Reflection Section
st.markdown("<h2 class='header'>📈 Reflect on Your Growth</h2>", unsafe_allow_html=True)
reflection = st.text_area("What valuable lesson did you learn today?")

if reflection:
    st.success(f"✨ Amazing! You've learned: {reflection}. Keep growing! 🌱")
else:
    st.info("Take a moment to reflect—every challenge teaches something new!")

# Achievements Section
st.markdown("<h2 class='header'>🏆 Celebrate Your Success</h2>", unsafe_allow_html=True)
achievement = st.text_area("What did you accomplish today?")

if achievement:
    st.success(f"🎉 Well done! You've achieved: {achievement}. Keep up the momentum!")
else:
    st.info("Every small step matters—celebrate your progress! 🥳")

# Footer
st.markdown("""
    <div class='footer'>
        🚀 Keep pushing forward! Believe in yourself and achieve greatness. 🌈<br>
        Thank you for using the Growth Mindset Challenge app. Have a fantastic day! 😊
    </div>
""", unsafe_allow_html=True)

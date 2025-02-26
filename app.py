# Streamlit
import streamlit as st

# Page Configuration (Fixed `page_icon` argument)
st.set_page_config(page_title="Growth Mindset Project", page_icon="🧠")

# App Title
st.title("Growth Mindset Challenge: Web App with Streamlit")

# Header & Introduction
st.header("🚀 Welcome to your Growth Journey!")
st.write("This is a simple web app that will help you develop a growth mindset. "
         "You will be able to track your progress and see how you are improving over time. Let's get started!")

# Quote Section
st.header("💡 Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill")

# Growth Mindset Goal Input
st.header("What's your growth mindset goal for today?")
user_input = st.text_input("Describe a challenge you're facing:")

# Conditional Statement
if user_input:
    st.success(f"You are facing: {user_input}. Keep pushing forward towards your goal! 🚀")
else:
    st.warning("Tell us about a challenge you're facing today.")

# Reflection Section
st.header("📈 Reflect on your Growth Mindset Journey")
reflection = st.text_area("What did you learn today?")

if reflection:
    st.success(f"✨ Great! You've learned: {reflection}. Keep up the good work! 🌟")
else:
    st.info("Reflecting on your day can help you grow. Share your difficulties.")

# Achievements Section
st.header("🏆 Celebrate Your Wins!")
achievement = st.text_area("What did you accomplish today?")

if achievement:
    st.success(f"💫 Congratulations! You've accomplished: {achievement}. Keep up the great work! 🎉")
else:
    st.info("Celebrate your wins, no matter how small. Share your accomplishments.😍")

# Footer
st.write("---")
st.write("🚀 Keep believing in yourself and remember that you can achieve anything you set your mind to. 🌈")
st.write("Thank you for using the Growth Mindset Challenge web app. Have a great day! 😊")

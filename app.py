# Import Streamlit
import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #1E1E1E; /* Dark background */
            color: white; /* White text */
        }
        .stApp {
            background-color: #1E1E1E; /* Full page dark theme */
        }
        h1, h2, h3 {
            color: #FF9800; /* Orange Headers */
        }
        .stTextInput, .stTextArea {
            background-color: #333; /* Dark Input Box */
            color: white;
        }
        .stTextInput>div>div>input, .stTextArea>div>textarea {
            color: white; /* White text inside input fields */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Configuration
st.set_page_config(page_title="Growth Mindset App", page_icon="🌟")

# App Title
st.title("🌟 Growth Mindset Challenge")

# Header & Introduction
st.header("🚀 Welcome to Your Growth Journey!")
st.write("Develop a **strong growth mindset** with this interactive app. Track your progress, "
         "reflect on challenges, and celebrate achievements. **Let's start!** 💪")

# Quote Section
st.header("💡 Daily Growth Mindset Quote")
st.markdown(
    '<p style="background-color:#FF9800;padding:10px;border-radius:5px;color:white;">'
    '✨ "Success is not final, failure is not fatal: It is the courage to continue that counts." - Winston Churchill</p>',
    unsafe_allow_html=True
)

# Growth Mindset Goal Input
st.header("🎯 Set Your Goal for Today")
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"You're facing: **{user_input}**. Keep pushing forward! 💪")
else:
    st.warning("Tell us about a challenge you're facing today.")

# Reflection Section
st.header("📈 Reflect on Your Journey")
reflection = st.text_area("What did you learn today?")

if reflection:
    st.success(f"🌟 Great insight! You've learned: **{reflection}**. Keep growing! 🚀")
else:
    st.info("Reflection helps you grow. Write something!")

# Achievements Section
st.header("🏆 Celebrate Your Wins!")
achievement = st.text_area("What did you accomplish today?")

if achievement:
    st.success(f"🎉 Awesome! You accomplished: **{achievement}**. Keep going! ✨")
else:
    st.info("Celebrate every achievement, big or small. Share your wins!")

# Footer
st.write("---")
st.write("🌟 Keep believing in yourself! You can achieve anything you set your mind to. 🚀")
st.write("**Thank you for using the Growth Mindset Challenge app. Have a great day!** 😊")

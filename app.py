#streamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset project", project_icon="🧠")
st.title("Growth Mindset Challenge: web App with Streamlit")

st.header("🚀 welcome to your growth journey!")
st.write("This is a simple web app that will help you to develop a growth mindset. You will be able to track your progress and see how you are improving over time. Let's get started!")

#quote section
st.header("💡Today's Growth Mindset Quote ")
st.write(" Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill")

st.header("What's your growth mindset goal for today?")
user_input = st.text_input("Describe a challenge you're facing:")


# conditinonal statement
if user_input:
    st.success(f" you are facing: {user_input}. keep pushing forward towards your goal! 🚀")
else:
    st.warning("Tell us about a challenge you're facing today.")

    #reflexing
    st.header("📈 Reflect on your growth mindset journey")
    reflection = st.text_area("What did you learn today?")

    if reflection:
        st.success(f" ✨Great! You've learned: {reflection}. Keep up the good work! 🌟")
    else:
        st.info("Reflecting on your day can help you grow. share your difficulties")


        # achievements
        st.header("🏆 Celebrate your Wins!")
        achievement = st.text_area("What did you accomplish today?")


        if achievement:
            st.success(f" 💫Congratulations! You've accomplished: {achievement}. Keep up the great work! 🎉")
        else:
            st.info("Celebrate your wins, no matter how small. Share your accomplishments.😍")


            #footer
            st.write("- - -")
            st.write("🚀 Keep believing in yourself and remember that you can achieve anything you set your mind to. 🌈")
            st.write("Thank you for using the Growth Mindset Challenge web app. Have a great day! 😊")
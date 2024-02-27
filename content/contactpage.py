from streamlit_lottie import st_lottie
import streamlit as st

def contactpage(contact_gif):
    col1, col2 = st.columns([0.5, 0.5])
    
    with col1:
        st.header("Contact Me")

        # Create a form for contact details
        st.subheader("Contact Form")
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        
        # Add a submit button
        if st.button("Submit"):
            # Handle form submission (you can add your logic here)
            if name and email and message:
                st.success("Message sent successfully!")
            else:
                st.warning("Please fill out the form above")
    
    with col2:
        st_lottie(contact_gif, speed=1)
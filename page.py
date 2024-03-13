import streamlit as st
import os
from streamlit_option_menu import option_menu
import requests as re
from streamlit_lottie import st_lottie
from Page.contactpage import contactpage
from Page.aboutpage import homepage
from Page.projects import projects_page
from PIL import Image
import json

load_image = Image.open('Content/images/starcraft2AI.png')

def clear_session_state():
    st.session_state.clear()

def read_json(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)
    return data

timeline_data = read_json("Page/JSON/timeline.json")
skillset_data = read_json("Page/JSON/skills.json")

def load_lottie_url(url: str):
    r = re.get(url)
    if r.status_code != 200:
        return None
    return r.json()

contact_gif = load_lottie_url("https://lottie.host/6f7ea4f5-712d-4baf-ad46-6dced0793d44/5zSIoOZqMc.json")
about_gif1 = load_lottie_url("https://lottie.host/748eae93-3a19-49b7-9bf0-6e1ddcc897ee/9fM3zwkrHA.json")
education_gif = load_lottie_url("https://lottie.host/9fb709e5-a981-4598-898a-8a2c1ccb9ab5/PIZDcfoLzr.json")
st.set_page_config(
        page_title="Tarush Portfolio",
        layout="wide"
    )

def load_images(image_path):
    img = Image.open(image_path)
    return img

def main():
    with st.container():
        selected = option_menu(menu_title = None, options = ['About', 'Experiences', 'Contact'],
                               icons = ['person','code-slash', 'chat-left-text-fill'],
                               orientation='horizontal')

    
    st.markdown(
        """
        <style>
            section[data-testid="stSidebar"] {
                width: 180px !important; # Set the width to your desired value
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.sidebar.image('Content/images/Profile.jpeg', use_column_width=True)
    st.markdown(
        """
        <style>
            /*.st-emotion-cache-1v0mbdj > img{
                border-radius: 50%;
            }*/
            div.st-emotion-cache-1owowqw:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > img:nth-child(1) {
                border-radius: 50%;
            }
        </style>
        """, unsafe_allow_html=True
    )
    
    st.sidebar.title("Tarush Singh")
    st.sidebar.markdown('---')
    st.sidebar.subheader("Public Profile")
    st.sidebar.markdown(
        """
        <a href="https://www.linkedin.com/in/tarush-singh-246144113/" target="_blank" style="display: inline-block; vertical-align: middle; text-decoration: none; color: white;">
            <img src="https://icons.getbootstrap.com/assets/icons/linkedin.svg" alt="LinkedIn" width="30" height="30" style="float: left; margin-right: 10px;">
            <span style="font-size: 16px; display: inline-block; vertical-align: middle; color: white;"> :LinkedIn</span>
        </a><br>
        <a href="https://github.com/TarushS-1996" target="_blank" style="display: inline-block; vertical-align: middle; text-decoration: none; color: white;">
            <img src="https://icons.getbootstrap.com/assets/icons/github.svg" alt="LinkedIn" width="30" height="30" style="float: left; margin-right: 10px;">
            <span style="font-size: 16px; display: inline-block; vertical-align: middle; color: white;"> :Github</span>
        </a><br>
        <a href="mailto:singh.tarus@northeastern.edu" target="_blank" style="display: inline-block; vertical-align: middle; text-decoration: none; color: white;">
            <img src="https://icons.getbootstrap.com/assets/icons/envelope-at-fill.svg" alt="LinkedIn" width="30" height="30" style="float: left; margin-right: 10px;">
            <span style="font-size: 16px; display: inline-block; vertical-align: middle; color: white;"> :Email</span>
        </a><br>
        <a href="https://medium.com/@singh.tarus" target="_blank" style="display: inline-block; vertical-align: middle; text-decoration: none; color: white;">
            <img src="https://icons.getbootstrap.com/assets/icons/medium.svg" alt="LinkedIn" width="30" height="30" style="float: left; margin-right: 10px;">
            <span style="font-size: 16px; display: inline-block; vertical-align: middle;"> :Medium</span>
        </a><br>
        """,
        unsafe_allow_html=True
    )
            
    if selected == 'About':
        clear_session_state()
        homepage(about_gif1, education_gif)
    elif selected == 'Experiences':
        clear_session_state()
        projects_page(timeLineData=timeline_data)
    elif selected == 'Contact':
        clear_session_state()
        contactpage(contact_gif)

if __name__ == '__main__':
    main()

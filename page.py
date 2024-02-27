import streamlit as st
import os
from streamlit_option_menu import option_menu
import requests as re
from streamlit_lottie import st_lottie
from content.contactpage import contactpage
from content.aboutpage import homepage

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

def main():
    with st.container():
        selected = option_menu(menu_title = None, options = ['About', 'Projects', 'Contact'],
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
    
    st.sidebar.image('Profile.jpeg', use_column_width=True)
    st.markdown(
        """
        <style>
            .st-emotion-cache-1v0mbdj > img{
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
            <span style="font-size: 16px; display: inline-block; vertical-align: middle; color: white;"> :Medium</span>
        </a><br>
        """,
        unsafe_allow_html=True
    )
            
    if selected == 'About':
        home_page()
    elif selected == 'Projects':
        projects_page()
    elif selected == 'Contact':
        contact_page()

def home_page():
    homepage(about_gif1, education_gif)    
    
def generate_links(category, count):
    links = []
    for i in range(1, count + 1):
        link_url = f"https://yourwebsite.com/{category}/{i}"
        link_text = f"{category} Link {i}"
        link = f'<a href="{link_url}">{link_text}</a>'
        links.append(link)
    return links

def projects_page():
    # Download resume
    st.subheader("Download Resume")
    resume_path = "Tarush.pdf"
    if os.path.exists(resume_path):
        st.download_button(
            label="Download Resume",
            data=open(resume_path, "rb").read(),
            file_name="Tarush_Resume.pdf",
            mime="application/pdf"
        )
    else:
        st.error("Resume file not found. Please check the file path.")
    st.markdown("---")  # Horizontal line to separate sections

    st.header("Projects")

    # Deep Learning section
    with st.expander("Deep Learning"):
        deep_learning_links = generate_links("Deep_Learning", 3)
        for link in deep_learning_links:
            st.markdown(link, unsafe_allow_html=True)

    # Data Science section
    with st.expander("Data Science"):
        data_science_links = generate_links("Data_Science", 4)
        for link in data_science_links:
            st.markdown(link, unsafe_allow_html=True)
            
    with st.expander("Robotics"):
        robotics_links = generate_links("Robotics", 2)
        for link in robotics_links:
            st.markdown(link, unsafe_allow_html=True)
    
    with st.expander("Software Development"):
        software_dev_links = generate_links("Software_Development", 1)
        for link in software_dev_links:
            st.markdown(link, unsafe_allow_html=True)


def contact_page():
    contactpage(contact_gif)

if __name__ == '__main__':
    main()
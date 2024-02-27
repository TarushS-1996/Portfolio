import streamlit as st
import os
from streamlit_option_menu import option_menu
import requests as re
from streamlit_lottie import st_lottie
from content.contactpage import contactpage
from content.aboutpage import homepage
from PIL import Image

load_image = Image.open('Projects/starcraft2AI.png')

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
        selected = option_menu(menu_title = None, options = ['About', 'Projects & Experiences', 'Contact'],
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
            <span style="font-size: 16px; display: inline-block; vertical-align: middle; color: white;"> :Medium</span>
        </a><br>
        """,
        unsafe_allow_html=True
    )
            
    if selected == 'About':
        home_page()
    elif selected == 'Projects & Experiences':
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
    st.header("Experience")
    experience_text = """
            <style>
                @media screen and (max-width: 600px) {
                    .content {
                        font-size: 14px;
                    }
                }
                @media screen and (min-width: 601px) and (max-width: 900px) {
                    .content {
                        font-size: 16px;
                    }
                }
                @media screen and (min-width: 901px) {
                    .content {
                        font-size: 18px;
                    }
                }
            </style>
            <div class="content">
                <strong>NLP Development Head</strong> - HappSales pvt ltd, Bangalore (Sep 2019 - Apr 2022)<br><br>
                &emsp; - Led NLP and deep learning projects for HappSales CRM product<br>
                &emsp; - Developed NLU models in RASA for app CRUD operations<br>
                &emsp; - Designed fine-tuned NER based SQL data fetching for QA<br>
                &emsp; - Managed AWS Lambda integration for NLP engine hosting<br>
                &emsp; - Enhanced productivity by 10-15% through UI and data entry optimizations<br>
                &emsp; - Produced comprehensive documentation for NLP tools and FAQs<br>
                <br>
            </div>
            """
            
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(experience_text, unsafe_allow_html=True)
    with col2:
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
        col1, col2 = st.columns([0.6, 2])
        with col1:
            st.image(load_image)   
        with col2:
            st.subheader("[StarCraft 2 AI]((https://photos.app.goo.gl/5moREbVnhaJ8UZVX6))")
            st.markdown(
                """<ul>
                    <li> Developed a StarCraft 2 AI using PySC2 and TensorFlow</li>
                    <li> Used opencv to highlight and map the important features of the game</li>
                    <li> Trained a CNN model to predict the game state and make decisions </li>
                    </ul>
                """
            , unsafe_allow_html=True)

    # Data Science section
    with st.expander("Data Science"):
        data_science_links = generate_links("Data_Science", 4)
        for link in data_science_links:
            st.markdown(link, unsafe_allow_html=True)
            
    with st.expander("Robotics"):
        link = "https://photos.app.goo.gl/zeH1Q63TvDr4zbnSA"
        col1, col2 = st.columns([0.6, 2])
        with col1:
            st.image('Projects/ros1.png')
        with col2:
            st.subheader("[ROS1 Simulation](https://photos.app.goo.gl/zeH1Q63TvDr4zbnSA)")
            st.markdown(
                """<ul>
                    <li> Designed a simple revolute joint in solidworks</li>
                    <li> Exported the package into ROS for simple simulation</li>
                    <li> Provided a detailed article on [Github]("https://github.com/TarushS-1996/Solidworks-to-gazebo") </li>
                    </ul>
                """
            , unsafe_allow_html=True)

    
    with st.expander("Software Development"):
        software_dev_links = generate_links("Software_Development", 1)
        for link in software_dev_links:
            st.markdown(link, unsafe_allow_html=True)
    

def contact_page():
    contactpage(contact_gif)

if __name__ == '__main__':
    main()
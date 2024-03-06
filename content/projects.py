from PIL import Image
import streamlit as st
import os


def load_images(image_path):
    img = Image.open(image_path)
    return img

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
    #col1, col2, col3 = st.columns([1, 1, 1])  
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
        col1, col2 = st.columns([0.4, 2])
        with col1:
            st.image(load_images("Projects/images/starcraft2AI.png"))   
        with col2:
            st.subheader("[StarCraft 2 AI](https://photos.app.goo.gl/5moREbVnhaJ8UZVX6)")
            st.markdown(
                """<ul>
                    <li> Developed a StarCraft 2 AI using PySC2 and TensorFlow</li>
                    <li> Used opencv to highlight and map the important features of the game</li>
                    <li> Trained a CNN model to predict the game state and make decisions </li>
                    </ul>
                """
            , unsafe_allow_html=True)
            
        col1, col2 = st.columns([0.4, 2])
        with col1:
            st.image(load_images('Projects/images/imagecap.png'))   
        with col2:
            st.subheader("[Image Caption AI](https://photos.app.goo.gl/5moREbVnhaJ8UZVX6)")
            st.markdown(
                """<ul>
                    <li> Studied Vision Transformers and its attention methods</li>
                    <li> Using the concepts applied and desinged an image caption system on COCO dataset</li>
                    <li> Trained the final model, evaluated the model and employed optimization techniques to improve accuracy of F1 score from 82% to 93%</li>
                    </ul>
                """
            , unsafe_allow_html=True)
        col1, col2 = st.columns([0.4, 2])
        with col1:
            st.image(load_images('Projects/images/wandb.png'))   
        with col2:
            st.subheader("[Weights & Biases tutorial](https://medium.com/@singh.tarus/intro-to-wandb-weights-and-biases-a-tool-for-hyperparameter-tuning-part-1-99cb418b4b62)")
            st.markdown(
                """<ul>
                    <li> Explored the concepts of hypertuning and performance fine tuning without impacting accuracy or overfitting</li>
                    <li> Used the Weights & Biases (WandB) to perform metric evaluations and provided a detailed article to the approaches and methodologies of using wandb</li>
                    </ul>
                """
            , unsafe_allow_html=True)

        col1, col2 = st.columns([0.4, 2])
        with col1:
            st.image(load_images('Projects/images/modelparam.png'))   
        with col2:
            st.subheader("[Model evaluation and parameter mapping](https://medium.com/@singh.tarus/a-dive-into-ml-models-feature-selection-and-interpretation-faf4bbcc075d)")
            st.markdown(
                """<ul>
                    <li> Examined concepts of data science dealing with feature selection, null hypothesis, correlations and algorithm selection</li>
                    <li> Validated the initial understanding of the machine learning predictions using SHAP analysis for improving performance</li>
                    <li> Provided a detailed article on the approaches and methodologies of using SHAP analysis in a medum article</li>
                    </ul>
                """
            , unsafe_allow_html=True)
            
    with st.expander("Robotics"):
        link = "https://www.researchgate.net/publication/330599023_Flamen_-_7_DOF_Robotic_Arm_to_Manipulate_a_Spanish_Fan"
        col1, col2 = st.columns([0.4, 2])
        with col1:
            st.image('Projects/images/ros1.png')
        with col2:
            st.subheader("[ROS1 Simulation](https://photos.app.goo.gl/LHr6Get7VZCGdkVCA)")
            st.markdown(
                """<ul>
                    <li> Designed a simple revolute joint in SolidWorks</li>
                    <li> Exported the package into ROS for simple simulation</li>
                    <li> Provided a detailed article on <a href="https://github.com/TarushS-1996/Solidworks-to-gazebo/tree/master">Github</a> </li>
                    </ul>
                """,
                unsafe_allow_html=True
            )
        col1, col2 = st.columns([0.4, 2])
        with col1:
            st.image('Projects/images/Athum.png')
        with col2:
            st.subheader("[Medical Telepresence Robot](https://photos.app.goo.gl/eVE9oMqJ6cy2tSRY9)")
            st.markdown(
                """<ul>
                    <li> Conducted a project on telepresence for medical application with a system requiring minimal hardware on the user end</li>
                    <li> Collaborated on using skeleton mapping to track user movements to be mimicked by a robotic torso over long distance</li>
                    <li> Provided visual feedback to user in VR and presented the findings in conference held at BITS Pilani </li>
                    </ul>
                """,
                unsafe_allow_html=True
            )
        
        col1, col2 = st.columns([0.4, 2])
        with col1:
            st.image('Projects/images/iros.png')
        with col2:
            st.subheader("[IROS Fan challenge](https://drive.google.com/drive/folders/17FSnqHi2I-QijiTSAWHSn0HVN1rAzhPd)")
            st.markdown(
                """<ul>
                    <li> Spearheaded the development of precise motion algorithm for manipulator arm for 2018 IROS fan challenge</li>
                    <li> Innovated and implemented image artificial intelligence algorithm for effective fan detection contributing to <a href = "https://www.iros2018.org/fan-robotic-challenge">Phase 1</a> victory</li>
                    <li> Acknowledged on IROS webpage, highlighting exceptional efficiency of motion and image system and IEEE publication <a href = "https://ieeexplore.ieee.org/document/8594129">(Link)</a></li>
                    </ul>
                """,
                unsafe_allow_html=True
            )
    
    with st.expander("Software Development"):
        col1, col2 = st.columns([0.4, 2])
        with col1:
            st.image('Projects/images/dominex.png')
        with col2:
            st.subheader("[Dominex](https://github.com/TarushS-1996/DrugLifeCycel-AED5100)")
            st.markdown(
                """<ul>
                    <li> Spearheaded a distributed drug development tracking app in Java enabling real time drug stage monitoring, time to market and FDA approval and implemented tailored UI pages for seamless user experience and data access</li>
                    <li> Engineered cross-organization collaborations fostering effective communication and coordination with insightful reporting<a href = "https://github.com/TarushS-1996/DrugLifeCycel-AED5100">(Link)</li>
                    </ul>
                """,
                unsafe_allow_html=True)
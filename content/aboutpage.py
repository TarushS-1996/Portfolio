import streamlit as st
from streamlit_lottie import st_lottie

def homepage(about_gif1, education_gif):
    st.title("Hi, I'm Tarush")

    # Create a layout with two columns
    col1, col2, col3 = st.columns([0.05, 0.5, 0.4])

    # In the first column, display the About Me text
    with col2:
        st.header("About Me")
        about_me_text = """
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
            <div class = "content">Hello, I'm Tarush Singh, a graduate student at Northeastern University with a passion for AI and robotics. 
            I excel in Java, Python, and deep learning tools like TensorFlow and PyTorch. During my tenure as an NLP Development Head at HappSales, 
            I designed solutions that streamlined application interactions and boosted productivity. 
            Now, I'm eager to explore innovative projects and contribute my skills to the exciting world of AI and robotics. 
            Let's connect and create something incredible together. Thank you!</div>
            """
        st.markdown(about_me_text, unsafe_allow_html=True)
        st.subheader("Experience")
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
        st.markdown(experience_text, unsafe_allow_html=True)

    # In the second column, display the image
    
    with col3:
        st_lottie(about_gif1, speed=1)
    
    
    st.markdown("---")
    st.subheader("Education")
    col6, col4, col5 = st.columns([0.05, 0.2, 0.6])
    with col5:
        st.markdown("""
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
            <div class = "content">
                - <strong>Masters in Information Systems</strong><br>
                &emsp; - Northeastern University, Boston MA (GPA: 3.65/4.0)<br>
                &emsp; - Aug 2022 - Apr 2024<br><br>
                - <strong>Bachelor of Science in Electronics and Communications Engineering</strong><br>
                &emsp; - SRM Institute of Science and Technology, Chennai<br>
                &emsp; - July 2014 - May 2018
            </div>""", 
            unsafe_allow_html=True
        )
    with col4:
        st_lottie(education_gif, speed=1)        
    
    st.markdown("---")
    
    st.subheader("Medals and Certifications")
    st.write("""
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
        <div class = "content">                
        - Presented a paper in IEEE IROS 2018 Fan challenge in Spain on 7-DOF robotic manipulator<br>
        - Won 2 golds and 1 bronze in “RoboGames 2018” held in the USA for Bipedal robots.<br>
        - Won 2nd position for the navigational shoes for visually impaired at Konvolve SRM University<br>
        - Won silver at ‘Indo US Robo League 2015‘ held in IIT Mumbai<br>
        - Deep Neural Networks May 2019 Improving Hyperparameter tuning, Regularization and Optimization Coursera Certification<br>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    st.subheader("Technical Skills")
    st.markdown("""
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
        <div class = "content">
            - <strong>Programming Language</strong>: Python, Java, HTML, SQL, C/C++, CSS<br><br>
            - <strong>Cloud</strong>: AWS Lambda, AWS EC2, AWS Elastic search, AWS Sagemaker, AWS SNS, Azure Function, Azure VM, REST API, Terraform, Kubernetes, FLASK, RESTful services<br><br>
            - <strong>AI Tools</strong>: Scikit-learn, OpenCV, Tensorflow, RASA, TfLearn, AutoML, Keras, Huggingface Transformers, XGBoost, GBM, NLTK, SpaCy, PyTorch, GLM, ResNet, Fast-RCNN, Alexnet, YOLO, Vision Transformers, ONNX, TensorRT<br><br>
            - <strong>Development tools</strong>: Postman, Git, Jupyter Notebook, Weights&Biases
        </div>""", 
        unsafe_allow_html=True
    )
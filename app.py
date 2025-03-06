import streamlit as st
import pandas as pd
from src.gen_ai.helper import GenAI
from src.Pipeline.prediction import Predication_Pipeline
import os 

from test import file


gen_ai = GenAI()
prediction_pipeline = Predication_Pipeline()


st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
    }
    h1 {
        color: #4a90e2;
    }
    h2 {
        color: #4a90e2;
    }
    .stButton button {
        background-color: #4a90e2;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #357abd;
    }
    .footer {
        text-align: center;
        padding: 10px;
        margin-top: 20px;
        font-size: 14px;
    }
    .footer a {
        color: #4a90e2;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.title("🍷 Wine Quality Prediction with AI")


st.sidebar.header("📊 Input Wine Data")

fixed_acidity = st.sidebar.number_input("Fixed Acidity", min_value=0.0, value=7.4)
volatile_acidity = st.sidebar.number_input("Volatile Acidity", min_value=0.0, value=0.7)
citric_acid = st.sidebar.number_input("Citric Acid", min_value=0.0, value=0.0)
chlorides = st.sidebar.number_input("Chlorides", min_value=0.0, value=0.076)
total_sulfur_dioxide = st.sidebar.number_input("Total Sulfur Dioxide", min_value=0, value=36)
density = st.sidebar.number_input("Density", min_value=0.0, value=0.9978)
pH = st.sidebar.number_input("pH", min_value=0.0, value=3.5100)
sulphates = st.sidebar.number_input("Sulphates", min_value=0.0, value=0.5600)
alcohol = st.sidebar.number_input("Alcohol", min_value=0.0, value=10.0)

input_data = {
    "fixed acidity": [fixed_acidity],
    "volatile acidity": [volatile_acidity],
    "citric acid": [citric_acid],
    "chlorides": [chlorides],
    "total sulfur dioxide": [total_sulfur_dioxide],
    "density": [density],
    "pH": [pH],
    "sulphates": [sulphates],
    "alcohol": [alcohol],
}

input_data_df = pd.DataFrame(input_data)


st.subheader("📋 Your Input Data")
st.dataframe(input_data_df, use_container_width=True)

if st.sidebar.button("🚀 Predict Wine Quality"):
    with st.spinner("🔮 Predicting wine quality..."):
        try:
            input_data_processed = prediction_pipeline.transform(input_data_df)
            prediction = prediction_pipeline.prediction(input_data_processed)
            
            
            if prediction == 1:
                quality = "Good"
            else:
                quality = "Bad"
            
            
            response = gen_ai.response(input_data=input_data_df.values.tolist())

            st.subheader("🎯 Prediction Result")
            st.success(f"**Wine Quality Prediction:** {quality}")

            st.subheader("💡 AI Suggestions")
            st.info(response)

        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")


st.sidebar.header("🛠️ Model Training")

if st.sidebar.button("🔧 Train Model"):
    with st.spinner("Training in progress..."):
        try:
            os.system("python main.py")
            st.success("🎉 Training completed successfully!")
            
            st.success(f'accuracy :{file}')
        except Exception as e:
            st.error(f"❌ Training failed: {str(e)}")


st.markdown("---")
st.markdown(
    """
    <div class="footer">
        <p>🛠️ Built with ❤️ by <strong>YourName</strong></p>
        <p>
            <a href="https://github.com/ldotmithu/FineWine-AI-Quality-Prediction-and-Personalized-Recommendations.git" target="_blank">
                <img src="https://img.icons8.com/ios-filled/50/000000/github.png" width="20" height="20"/>
                GitHub
            </a>
            &nbsp;|&nbsp;
            <a href="https://www.linkedin.com/in/YourLinkedIn/" target="_blank">
                <img src="https://img.icons8.com/ios-filled/50/000000/linkedin.png" width="20" height="20"/>
                LinkedIn
            </a>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("---")

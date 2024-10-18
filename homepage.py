import streamlit as st
from HeartPrediction import show_heart_prediction
from KidneyPrediction import show_kidney_prediction

# Streamlit page configuration
st.set_page_config(
    page_title="Multi Disease Prediction System",
    page_icon=":hospital:",
    layout="wide"
)


st.markdown(
    """
    <style>
    body {
        color: white;
        background-color: #121212;
    }
    .sidebar .sidebar-content {
        width: 250px;
        position: fixed;
        height: 100vh;
        top: 0;
        left: 0;
        overflow-y: auto;
        padding-top: 20px;
    }
    .reportview-container .main {
        margin-left: 260px;
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Multi Disease Prediction System")


with st.sidebar:
    st.markdown("## Predictions")
    selected_option = st.radio("", ( "Home Page", "Heart Attack Prediction", "Kidney Disease Prediction","Brain Tumor Prediction"))

if selected_option == "Home Page":
    st.markdown("### Welcome!  This system allows you to predict various diseases such as heart attacks, kidney diseases, and Brain Tumor via MRI Scan. Simply select the type of prediction you want to make from the sidebar.")
    st.image("Diagnostic_imaging_mobile.svg", use_column_width=True)
elif selected_option == "Heart Attack Prediction":
    show_heart_prediction()
elif selected_option == "Kidney Disease Prediction":
    show_kidney_prediction()




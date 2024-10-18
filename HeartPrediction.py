# importing libraries
import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('heart_model.sav', 'rb'))

def heart_predict(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction
def show_heart_prediction():
    st.title('Heart Attack Predictor')
    st.markdown("#### Enter Your Symptoms")
    name =   st.text_input("Name", "", placeholder="Enter Patient's Name")
    age = st.number_input('Age', min_value=0, max_value=110, value=30, step=1)
    gender_options = ['Male', 'Female']
    gender = st.radio('Gender', gender_options)
    if gender == 'Male':
      gender_value = 1.0
    else:
      gender_value = 0.0
    cp_options = {'Typical Angina': 1.0, 'Atypical Angina': 2.0, 'Non-Anginal': 3.0, 'Asymptomatic': 4.0}
    chest_pain = st.selectbox('Chest Pain Type', list(cp_options.keys()))
    chest_pain_value = cp_options[chest_pain]
    trestbps = st.number_input('Resting Systolic Blood Pressure(at the time of admission)', min_value=50, max_value=250, value=120, step=1)
    chol = st.number_input('Serum Cholestrol Level', min_value=0.0, max_value=700.0, value=126.0, step=1.0)
    fbs_value = st.radio("Was fasting blood sugar level >120mg/dl?", ("No", "Yes"))
    fbs = 1.0 if fbs_value == "Yes" else 0.0
    restecg_options = {'Normal': 0.0, 'ST-T Abnormality': 1.0, 'LV Hypertrophy': 2.0}
    restecg = st.selectbox('Resting Electrocardiographic Results', list(restecg_options.keys()))
    restecg_value = restecg_options[restecg]
    thalach = st.number_input('Maximum Heart Rate Acheived', min_value=10, max_value=202, value=71, step=1)
    exang_options = {"No": 0.0, "Yes": 1.0}
    exang = st.selectbox('Do you experience chest pain during exercise?', list(exang_options.keys()))
    exang_value = exang_options[exang]
    oldpeak = st.number_input('ST Depression induced by Exercise relative to Rest', min_value=0.0, max_value=8.0, value=0.0, step=0.1)
    slope_options = {'Upsloping': 1.0, 'Flat': 2.0, 'Downsloping': 3.0}
    slope = st.selectbox('The Slope of the Peak Exercise ST Segment', list(slope_options.keys()))
    slope_value = slope_options[slope]
    ca_options = {'No': 0.0, 'Yes': 1.0}
    ca = st.selectbox('Number of Major Vessels Colored by flouroscopy', list(ca_options.keys()))
    ca_value = ca_options[ca]
    thal_options = {'Normal': 1.0, 'Fixed Defect': 2.0, 'Reversible Defect': 3.0}
    thal = st.selectbox('Thalassemia', list(thal_options.keys()), index=0)
    thal_value = thal_options[thal]
    input_data = [age, gender_value, chest_pain_value, trestbps, chol, fbs, restecg_value, thalach, exang_value, oldpeak, slope_value, ca_value, thal_value]
    
   
    if st.button('Predict'):
        input_data = list(map(float, input_data))
        prediction = heart_predict(input_data)
        if prediction[0] == 0:
            st.write("The Person does not have a Heart Disease")
        else:
            st.write("The Person has Heart Disease")

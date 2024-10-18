# importing libraries
import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open('kidney.pkl', 'rb'))

def kidney_predict(input_data):
    prediction = loaded_model.predict(input_data)
    return prediction

def show_kidney_prediction():
  
    st.title('Kidney Disease Predictor')
    st.markdown("Enter Your Symptoms")

        
    age = st.number_input('What is your age?', min_value=18, max_value=100, step=1)
    blood_pressure = st.number_input('What is your blood pressure? (mm/Hg)', min_value=60, max_value=220, step=1)
    specific_gravity = st.number_input('What is the specific gravity of your urine?', min_value=1.000, max_value=1.025)
    albumin = st.number_input('What is your urine albumin level?', min_value=0, max_value=5, step=1)
    red_blood_cells = st.selectbox('What is the state of your red blood cells?', ['Normal', 'Abnormal'])
    pus_cell = st.selectbox('What is the state of your pus cells?', ['Normal', 'Abnormal'])
    pus_cell_clumps = st.selectbox('Do you have pus cell clumps?', ['Absent', 'Present'])
    bacteria = st.selectbox('Do you have bacteria in your urine?', ['Absent', 'Present'])
    blood_glucose_random = st.number_input('What is your random blood glucose level? (bgr in mgs/dl)', min_value=70, max_value=500, step=1)
    blood_urea = st.number_input('What is your blood urea level? (bu in mgs/dl)', min_value=7, max_value=250, step=1)
    serum_creatinine = st.number_input('What is your serum creatinine level? (sc in mgs/dl)', min_value=0.5, max_value=15.0, step=0.1)
    sodium = st.number_input('What is your sodium level?', min_value=120, max_value=160, step=1)
    potassium = st.number_input('What is your potassium level?', min_value=2, max_value=7, step=1)
    haemoglobin = st.number_input('What is your haemoglobin level?', min_value=10, max_value=20, step=1)
    packed_cell_volume = st.number_input('What is your packed cell volume?', min_value=30, max_value=60, step=1)
    white_blood_cell_count = st.number_input('What is your white blood cell count?', min_value=3000, max_value=15000, step=1)
    red_blood_cell_count = st.number_input('What is your red blood cell count?', min_value=3, max_value=8, step=1)
    hypertension = st.selectbox('Do you have hypertension?', ['Absent', 'Present'])
    diabetes_mellitus = st.selectbox('Do you have diabetes mellitus?', ['Absent', 'Present'])
    coronary_artery_disease = st.selectbox('Do you have coronary artery disease?', ['Absent', 'Present'])
    appetite = st.selectbox('How is your appetite?', ['Good', 'Poor'])
    peda_edema = st.selectbox('Do you have pedal edema?', ['No', 'Yes'])
    aanemia = st.selectbox('Do you have anemia?', ['No', 'Yes'])

   
    if st.button('Predict'):
       
        red_blood_cells = 1 if pus_cell_clumps == 'Normal' else 0
        pus_cell = 1 if pus_cell_clumps == 'Normal' else 0
        pus_cell_clumps_value = 1 if pus_cell_clumps == 'Present' else 0
        bacteria_value = 1 if bacteria == 'Present' else 0
        hypertension_value = 1 if hypertension == 'Present' else 0
        diabetes_mellitus_value = 1 if diabetes_mellitus == 'Present' else 0
        coronary_artery_disease_value = 1 if coronary_artery_disease == 'Present' else 0
        appetite_value = 1 if appetite == 'Good' else 0
        peda_edema_value = 1 if peda_edema == 'Yes' else 0
        aanemia_value = 1 if aanemia == 'Yes' else 0

        input_data = [
            age, blood_pressure, specific_gravity, albumin, red_blood_cells, pus_cell,
            pus_cell_clumps_value, bacteria_value, blood_glucose_random, blood_urea, serum_creatinine,
            sodium, potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count,
            hypertension_value, diabetes_mellitus_value, coronary_artery_disease_value, appetite_value,
            peda_edema_value, aanemia_value
        ]
        
        input_data = np.array(input_data).reshape(1, -1)
       
        prediction = kidney_predict(input_data)
        if prediction[0] == 0:
            st.write("You are unlikely to have Kidney Disease")
        else:
            st.write("You are likely to have Kidney Disease")

import streamlit as st
from tensorflow.keras.applications import VGG19
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.models import Model
import cv2
import numpy as np
from PIL import Image
from werkzeug.utils import secure_filename

# Load pre-trained VGG19 model
base_model = VGG19(include_top=False, input_shape=(240, 240, 3))
x = base_model.output
flat = Flatten()(x)
class_1 = Dense(4608, activation='relu')(flat)
drop_out = Dropout(0.2)(class_1)
class_2 = Dense(1152, activation='relu')(drop_out)
output = Dense(2, activation='softmax')(class_2)
model_03 = Model(base_model.inputs, output)
model_03.load_weights('vgg19_model_02.h5')

# Function to get class name
def get_className(classNo):
    if classNo == 0:
        return "No the patient does not have Brain Tumor"
    elif classNo == 1:
        return "Yes the patient has Brain Tumor"

# Function to get prediction
def get_result(img):
    image = cv2.imread(img)
    image = Image.fromarray(image, 'RGB').resize((240, 240))
    image = np.array(image)
    input_img = np.expand_dims(image, axis=0)
    result = model_03.predict(input_img)
    result01 = np.argmax(result, axis=1)
    return result01

# Streamlit app
def show_Brain_pred():
    st.title("Brain Tumor Detection")

    uploaded_file = st.file_uploader("Upload an Image of Brain MRI Scan", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        st.write("")

        file_path = "uploaded_image.png"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if st.button("Predict"):
            value = get_result(file_path)
            result = get_className(value[0])
            st.write("Prediction:", result)


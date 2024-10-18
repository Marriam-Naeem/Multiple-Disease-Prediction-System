# Multiple Disease Prediction System

The **Multiple Disease Prediction System** is a machine learning-based web application that predicts the likelihood of multiple diseases, including heart disease, diabetes, and brain tumors. It uses advanced models to provide users with accurate and personalized predictions, including image-based detection for brain tumors.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Contributing](#contributing)

## Features
- Predicts multiple diseases based on user inputs:
  - Heart Disease
  - Diabetes
  - Brain Tumor (using image detection)
- Easy-to-use interface
- Real-time predictions and results
- Image-based prediction for brain tumor detection
- Data visualization for prediction results

## Tech Stack
- **Frontend**: Streamlit (for the web interface)
- **Backend**: Python
- **Libraries**: 
  - `pandas` for data manipulation
  - `scikit-learn` for building machine learning models
  - `numpy` for numerical computations
  - `matplotlib` and `seaborn` for data visualization
  - `TensorFlow`/`Keras` for deep learning and image processing (for brain tumor detection)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Marriam-Naeem/Multiple-Disease-Prediction-System.git

2. Navigate to the project directory
   ```bash
   cd Multiple-Disease-Prediction-System

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

**Run the Streamlit application:**

```bash
streamlit run homepage.py

```
### Accessing the Application

1. **Open your web browser.**
2. **Go to [http://localhost:8501](http://localhost:8501).**

### Prediction

1. Heart Disease and Diabetes: Input the required health data for prediction.
2. Brain Tumor Detection:Upload an MRI image.

The system will display the likelihood of the selected disease based on your inputs or image.

## Model Details

The system uses the following machine learning models for disease prediction:

* **Heart Disease:** Various machine learning models are applied, and their accuracy is checked. Please see the notebook for detailed comparisons.
* **Kidney Disease:** Multiple machine learning models are tested for accuracy. Refer to the notebook for performance metrics.
* **Diabetes:** Random Forest Classifier
* **Brain Tumor:** VGG-19 model for image classification

The brain tumor detection model is trained using MRI image datasets and fine-tuned for accurate tumor classification.


## Contributing

Contributions are welcome! If you have any suggestions or improvements, please create an issue or submit a pull request.

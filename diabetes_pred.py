import pickle
import streamlit as st
import numpy as np

# Load models
def load_model(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model

def run():
    # Load model
    diabetes_model = load_model('./Models/diabetes_model.pkl')

    # Diabetes Prediction Page
    st.title('Diabetes Prediction')

    # Input fields
    with st.form('diabetes_input_form'):
        st.header('Enter Patient Information')

        Pregnancies = st.slider('Number of Pregnancies', min_value=0, max_value=17, step=1, format="%d")
        Glucose = st.slider('Glucose Level (mg/dL)', min_value=0, max_value=200, step=1, format="%d")
        BloodPressure = st.slider('Blood Pressure (mm Hg)', min_value=0, max_value=122, step=1, format="%d")
        SkinThickness = st.slider('Skin Thickness (mm)', min_value=0, max_value=99, step=1, format="%d")
        Insulin = st.slider('Insulin Level (μU/ml)', min_value=0, max_value=846, step=1, format="%d")
        BMI = st.slider('BMI (kg/m²)', min_value=0.0, max_value=67.1, step=0.1, format="%.1f")
        DiabetesPedigreeFunction = st.slider('Diabetes Pedigree Function', min_value=0.0, max_value=2.4, step=0.01, format="%.2f")
        Age = st.slider('Age of the Person', min_value=0, max_value=81, step=1, format="%d")

        submit_button = st.form_submit_button(label='Diabetes Test Result')

    # Prediction
    if submit_button:
        features = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        features_arr = np.array(features)
        features_2d = features_arr.reshape(1, -1)
        # Predict directly with raw data
        prediction = diabetes_model.predict(features_2d)
        if prediction[0] == 0:
            st.success('The individual is Non-Diabetic. However, it is advisable to maintain a healthy lifestyle and monitor blood sugar levels regularly.')
            st.write('Lifestyle Changes:')
            st.write('- Follow a balanced diet rich in fruits, vegetables, and whole grains.')
            st.write('- Engage in regular physical activity such as walking, cycling, or swimming.')
            st.write('- Monitor blood sugar levels as advised by a healthcare professional.')
            st.write('Please consult a healthcare professional for personalized guidance and recommendations.')
        else:
            st.error('The person is Diabetic. Please consult a healthcare professional for further evaluation and management.')
            st.write('Lifestyle Modifications and Tips for Diabetic Patients:')
            st.write('- Follow a balanced diet with portion control, limiting sugary and high-carbohydrate foods.')
            st.write('- Engage in regular physical activity, such as brisk walking, jogging, or yoga, for at least 30 minutes most days of the week.')
            st.write('- Monitor blood sugar levels regularly and keep a record.')
            st.write('- Take medications as prescribed by a healthcare professional.')
            st.write('- Manage stress through relaxation techniques such as deep breathing, meditation, or yoga.')
            st.write('- Ensure regular follow-ups with healthcare providers for monitoring and adjustments to treatment plans as needed.')

if __name__ == '__main__':
    run()

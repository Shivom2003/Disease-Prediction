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
    heart_model = load_model('./Models/heart_disease_model.pkl')
    
    # Heart Disease Prediction Page
    st.title('Heart Disease Prediction')

    # Input fields
    with st.form('heart_disease_input_form'):
        st.header('Enter Patient Information')

        Age = st.slider('Age', min_value=0, max_value=100, step=1)
        Sex = st.selectbox('Sex', ['Female', 'Male'])
        ChestPainType = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
        RestingBloodPressure = st.slider('Resting Blood Pressure (mm Hg)', min_value=90, max_value=200, step=1)
        Cholesterol = st.slider('Cholesterol (mg/dl)', min_value=100, max_value=600, step=1)
        FastingBloodSugar = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['False', 'True'])
        RestingECG = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'])
        MaxHeartRate = st.slider('Maximum Heart Rate Achieved', min_value=60, max_value=220, step=1)
        ExerciseInducedAngina = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
        STDepression = st.slider('ST Depression Induced by Exercise', min_value=0.0, max_value=6.0, step=0.1)
        Slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
        NumMajorVessels = st.slider('Number of Major Vessels Colored by Fluoroscopy', min_value=0, max_value=3, step=1)
        Thalassemia = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

        submit_button = st.form_submit_button(label='Heart Disease Test Result')

    # Prediction
    if submit_button:
        # Transform categorical features
        Sex = 1 if Sex == 'Male' else 0
        ChestPainType = ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'].index(ChestPainType)
        FastingBloodSugar = 1 if FastingBloodSugar == 'True' else 0
        RestingECG = ['Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'].index(RestingECG)
        ExerciseInducedAngina = 1 if ExerciseInducedAngina == 'Yes' else 0
        Slope = ['Upsloping', 'Flat', 'Downsloping'].index(Slope)
        Thalassemia = ['Normal', 'Fixed Defect', 'Reversible Defect'].index(Thalassemia)

        # Create input data array
        input_data = np.array([[Age, Sex, ChestPainType, RestingBloodPressure, Cholesterol, FastingBloodSugar,
                                RestingECG, MaxHeartRate, ExerciseInducedAngina, STDepression, Slope,
                                NumMajorVessels, Thalassemia]])

        # Perform prediction
        prediction = heart_model.predict(input_data)
        if prediction[0] == 0:
            st.success('The individual does not have heart disease. Follow regular routine and healthy lifestyle.')
        else:
            st.error('The individual has heart disease. Please consult a healthcare professional immediately.')
            st.write('Recommended Precautionary Measures and Lifestyle Changes:')
            st.write('- Monitor and maintain a healthy blood pressure and cholesterol level.')
            st.write('- Avoid smoking and limit alcohol consumption.')
            st.write('- Maintain a healthy weight, follow a heart-healthy diet rich in fruits, vegetables, and whole grains.')
            st.write('- Engage in regular physical activity, aim for at least 150 minutes of moderate aerobic activity or 75 minutes of vigorous activity per week.')
            st.write('- Manage stress through relaxation techniques such as deep breathing, meditation, or yoga.')
            st.write('- Regularly check-up with your cardiologist and adhere strictly to prescribed medications and therapies.')
            st.write('- Consider participation in cardiac rehabilitation as advised by your doctor.')

if __name__ == '__main__':
    run()

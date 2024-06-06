import pickle
import streamlit as st
import numpy as np

# Load model
def load_model(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model

def run():
    # Load model
    asthma_model = load_model('./Models/asthma_model.pkl')

    # Asthma Prediction Page
    st.title('Asthma Disease Prediction')

    # Input fields
    with st.form('asthma_input_form'):
        st.header('Enter Patient Information')

        Tiredness = st.selectbox('Tiredness', ['Yes', 'No'])
        Dry_Cough = st.selectbox('Dry Cough', ['Yes', 'No'])
        Difficulty_in_Breathing = st.selectbox('Difficulty in Breathing', ['Yes', 'No'])
        Sore_Throat = st.selectbox('Sore Throat', ['Yes', 'No'])
        None_Symptom = st.selectbox('None Symptom', ['Yes', 'No'])
        Pains = st.selectbox('Pains', ['Yes', 'No'])
        Nasal_Congestion = st.selectbox('Nasal Congestion', ['Yes', 'No'])
        Runny_Nose = st.selectbox('Runny Nose', ['Yes', 'No'])
        None_Experiencing = st.selectbox('None Experiencing', ['Yes', 'No'])
        Age = st.selectbox('Age', ['0-9', '10-19', '20-24', '25-59', '60+'])
        Gender = st.selectbox('Gender', ['Female', 'Male'])

        submit_button = st.form_submit_button(label='Asthma Test Result')

    # Prediction
    if submit_button:
        # Transform categorical features
        Tiredness = 1 if Tiredness == 'Yes' else 0
        Dry_Cough = 1 if Dry_Cough == 'Yes' else 0
        Difficulty_in_Breathing = 1 if Difficulty_in_Breathing == 'Yes' else 0
        Sore_Throat = 1 if Sore_Throat == 'Yes' else 0
        None_Symptom = 1 if None_Symptom == 'Yes' else 0
        Pains = 1 if Pains == 'Yes' else 0
        Nasal_Congestion = 1 if Nasal_Congestion == 'Yes' else 0
        Runny_Nose = 1 if Runny_Nose == 'Yes' else 0
        None_Experiencing = 1 if None_Experiencing == 'Yes' else 0
        Age_0_9 = 1 if Age == '0-9' else 0
        Age_10_19 = 1 if Age == '10-19' else 0
        Age_20_24 = 1 if Age == '20-24' else 0
        Age_25_59 = 1 if Age == '25-59' else 0
        Age_60_plus = 1 if Age == '60+' else 0
        Gender_Female = 1 if Gender == 'Female' else 0
        Gender_Male = 1 if Gender == 'Male' else 0

        # Create input data array
        input_data = np.array([[Tiredness, Dry_Cough, Difficulty_in_Breathing, Sore_Throat, None_Symptom,
                                Pains, Nasal_Congestion, Runny_Nose, None_Experiencing, 
                                Age_0_9, Age_10_19, Age_20_24, Age_25_59, Age_60_plus, 
                                Gender_Female, Gender_Male]])

        # Perform prediction
        prediction = asthma_model.predict(input_data)
        if prediction[0] == 0:
            st.error('The person is Asthmatic. Please consult a healthcare professional for further evaluation and guidance.')
            st.write('Lifestyle Changes:')
            st.write('- Avoid triggers such as smoke, dust, and allergens.')
            st.write('- Maintain a healthy weight and exercise regularly.')
            st.write('- Practice stress-relieving techniques such as yoga and meditation.')
            st.write('Dietary Recommendations:')
            st.write('- Consume a diet rich in fruits, vegetables, and omega-3 fatty acids.')
            st.write('- Limit intake of processed foods and sugary beverages.')
            st.write('Alternative Therapies:')
            st.write('- Consider incorporating breathing exercises such as Pranayama.')
            st.write('- Explore acupuncture or herbal remedies under the guidance of a qualified practitioner.')
            st.write('Please note that the above suggestions are for informational purposes only and should not replace medical advice.')
        else:
            st.success('The individual is Non-Asthmatic. Maintain healthy habits and consult a healthcare professional if symptoms persist.')

if __name__ == '__main__':
    run()

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
    liver_model = load_model('./Models/liver_disease_model.pkl')
    
    # Liver Disease Prediction Page
    st.title('Liver Disease Prediction')

    # Input fields
    with st.form('liver_disease_input_form'):
        st.header('Enter Patient Information')

        Age = st.slider('Age', min_value=0, max_value=100, step=1)
        Gender = st.selectbox('Gender', ['Male', 'Female'])
        Total_Bilirubin = st.slider('Total Bilirubin', min_value=0.0, max_value=100.0, step=0.1)
        Direct_Bilirubin = st.slider('Direct Bilirubin', min_value=0.0, max_value=100.0, step=0.1)
        Alkaline_Phosphotase = st.slider('Alkaline Phosphotase', min_value=0, max_value=1000, step=1)
        Alamine_Aminotransferase = st.slider('Alamine Aminotransferase', min_value=0, max_value=1000, step=1)
        Aspartate_Aminotransferase = st.slider('Aspartate Aminotransferase', min_value=0, max_value=1000, step=1)
        Total_Protiens = st.slider('Total Proteins', min_value=0.0, max_value=20.0, step=0.1)
        Albumin = st.slider('Albumin', min_value=0.0, max_value=20.0, step=0.1)
        Albumin_and_Globulin_Ratio = st.slider('Albumin and Globulin Ratio', min_value=0.0, max_value=10.0, step=0.1)

        submit_button = st.form_submit_button(label='Liver Disease Test Result')

    # Prediction
    if submit_button:
        # Transform gender to numeric
        Gender = 1 if Gender == 'Male' else 0

        # Create input data array
        input_data = [[Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase,
                       Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens,
                       Albumin, Albumin_and_Globulin_Ratio]]
        
        input_data_array = np.array(input_data)

        # Perform prediction
        prediction = liver_model.predict(input_data_array)
        if prediction[0] == 0:
            st.success('The individual does not have liver disease. Continuing regular check-ups and maintaining a healthy lifestyle is recommended.')
        else:
            st.error('The individual has liver disease. Please consult a healthcare professional immediately.')
            st.write('Recommended Precautionary Measures and Lifestyle Changes:')
            st.write('- Maintain a balanced diet low in fats and rich in fruits and vegetables.')
            st.write('- Avoid alcohol consumption and smoking.')
            st.write('- Regularly exercise, consider activities like walking or swimming.')
            st.write('- Practice stress management techniques like yoga and meditation.')
            st.write('- Ensure adequate sleep each night.')
            st.write('- Regularly monitor your health and schedule follow-up appointments with a healthcare provider.')
            st.write('- Discuss with your doctor about medications and therapies that can help manage your condition.')

if __name__ == '__main__':
    run()

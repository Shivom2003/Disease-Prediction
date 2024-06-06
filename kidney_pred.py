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
    kidney_model = load_model('./Models/kidney_disease_model.pkl')

    st.title('Kidney Disease Prediction')
    
    # Input fields
    with st.form('kidney_disease_input_form'):
        st.header('Enter Patient Information')

        age = st.slider('Age', min_value=0, max_value=100, step=1)
        bp = st.slider('Blood Pressure (mm/Hg)', min_value=0, max_value=250, step=1)
        sg = st.slider('Specific Gravity', min_value=1.0, max_value=2.0, step=0.01)
        al = st.slider('Albumin', min_value=0, max_value=5, step=1)
        su = st.slider('Sugar', min_value=0, max_value=5, step=1)
        rbc = st.selectbox('Red Blood Cells', ['normal', 'abnormal'])
        pc = st.selectbox('Pus Cells', ['normal', 'abnormal'])
        pcc = st.selectbox('Pus Cell Clumps', ['present', 'notpresent'])
        ba = st.selectbox('Bacteria', ['present', 'notpresent'])
        bgr = st.slider('Blood Glucose Random (mgs/dL)', min_value=0, max_value=500, step=1)
        bu = st.slider('Blood Urea (mgs/dL)', min_value=0, max_value=500, step=1)
        sc = st.slider('Serum Creatinine (mgs/dL)', min_value=0.0, max_value=15.0, step=0.1)
        sod = st.slider('Sodium (mEq/L)', min_value=0, max_value=200, step=1)
        pot = st.slider('Potassium (mEq/L)', min_value=0.0, max_value=20.0, step=0.1)
        hemo = st.slider('Hemoglobin (gms)', min_value=0.0, max_value=25.0, step=0.1)
        pcv = st.slider('Packed Cell Volume (%)', min_value=0, max_value=100, step=1)
        wc = st.slider('White Blood Cell Count (cells/cmm)', min_value=0, max_value=25000, step=1)
        rc = st.slider('Red Blood Cell Count (millions/cmm)', min_value=0.0, max_value=10.0, step=0.1)
        htn = st.selectbox('Hypertension', ['yes', 'no'])
        dm = st.selectbox('Diabetes Mellitus', ['yes', 'no'])
        cad = st.selectbox('Coronary Artery Disease', ['yes', 'no'])
        appet = st.selectbox('Appetite', ['good', 'poor'])
        pe = st.selectbox('Pedal Edema', ['yes', 'no'])
        ane = st.selectbox('Anemia', ['yes', 'no'])

        submit_button = st.form_submit_button(label='Kidney Disease Test Result')

    # Prediction
    if submit_button:
        # Convert categorical variables to numerical
        rbc = 1 if rbc == 'abnormal' else 0
        pc = 1 if pc == 'abnormal' else 0
        pcc = 1 if pcc == 'present' else 0
        ba = 1 if ba == 'present' else 0
        htn = 1 if htn == 'yes' else 0
        dm = 1 if dm == 'yes' else 0
        cad = 1 if cad == 'yes' else 0
        appet = 1 if appet == 'good' else 0
        pe = 1 if pe == 'yes' else 0
        ane = 1 if ane == 'yes' else 0

        # Create input data array
        input_data = [[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]]
        
        input_data_array = np.array(input_data)

        # Perform prediction
        prediction = kidney_model.predict(input_data_array)
        if prediction[0] == 0:
            st.success('The individual does not have kidney disease')
        else:
            st.error('The individual has kidney disease')
            st.write('It is advisable for the individual to seek medical attention promptly and follow the advice of healthcare professionals. Lifestyle modifications such as maintaining a healthy diet, staying hydrated, avoiding smoking and excessive alcohol consumption, and engaging in regular physical activity can help manage kidney disease. Additionally, incorporating stress-reducing practices like yoga and meditation into daily routines may be beneficial. Medications and treatment options prescribed by healthcare providers should be followed diligently to control symptoms and prevent complications. Regular monitoring of kidney function and routine check-ups are essential for managing kidney disease effectively and improving overall health.')
            st.write('Precautions and Recommendations:')
            st.write('- Maintain a balanced diet low in salt, processed foods, and saturated fats, and high in fruits, vegetables, and whole grains.')
            st.write('- Stay hydrated by drinking plenty of water throughout the day.')
            st.write('- Avoid smoking and limit alcohol consumption.')
            st.write('- Engage in regular physical activity such as walking, swimming, or cycling for at least 30 minutes most days of the week.')
            st.write('- Practice stress management techniques such as yoga, meditation, or deep breathing exercises.')
            st.write('- Follow medication regimens as prescribed by healthcare providers.')
            st.write('- Monitor blood pressure, blood sugar, and cholesterol levels regularly as advised by healthcare professionals.')
            st.write('- Attend regular follow-up appointments with healthcare providers to track kidney function and adjust treatment plans as needed.')

if __name__ == '__main__':
    run()

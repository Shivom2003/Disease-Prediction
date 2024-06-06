# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:40:35 2024

@author: shivom
"""

import streamlit as st
from streamlit_option_menu import option_menu

# Import other disease prediction files
import asthma_pred
import heart_pred
import kidney_pred
import liver_pred
import diabetes_pred

# sidebar for navigation

with st.sidebar:
    
    select = option_menu('Disease Prediction System using ML',
                         
                         ['Asthma Prediction',                          
                          'Heart Disease Prediction',
                          'Kidney Disease Prediction',
                          'Liver Disease Prediction',
                          'Diabetes Prediction'],
                         
                         icons = ['lungs','heart-pulse','bandaid','droplet-half','activity'],
                         
                         default_index = 0)
    
# Display selected disease prediction page
if select == 'Asthma Prediction':
    asthma_pred.run()
elif select == 'Heart Disease Prediction':
    heart_pred.run()
elif select == 'Kidney Disease Prediction':
    kidney_pred.run()
elif select == 'Liver Disease Prediction':
    liver_pred.run()
elif select == 'Diabetes Prediction':
    diabetes_pred.run()
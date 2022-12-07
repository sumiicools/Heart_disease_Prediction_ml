# -*- coding: utf-8 -*-

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Disease Prediction System',
                          
                          ['Heart Disease Prediction'],
                          icons=['heart'],
                          default_index=0)

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    selected = option_menu('Heart Disease Prediction using ML',['Heart Disease Prediction'],icons=['heart'],default_index=0)

    st.title('Heart Disease Prediction using ML')
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex (M=1 , F=0)')
        
    with col1:
        cp = st.text_input('Chest Pain types (0-4)')
        
    with col2:
        trestbps = st.text_input('Resting Blood Pressure (100-200)')
        
    with col1:
        chol = st.text_input('Serum Cholestoral in mg/dl (200 - 400)')
        
    with col2:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl - (1) / (0)')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (0  or 1)')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved (71-202)')
        
    with col1:
        exang = st.text_input('Exercise Induced Angina (0 or 1)')
        
    with col2:
        oldpeak = st.text_input('ST depression induced by exercise (0-6.2)')
        
    with col1:
        slope = st.text_input('Slope of the peak exercise ST segment (0-2)')
        
    with col2:
        ca = st.text_input('Major vessels colored by flourosopy ()')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)

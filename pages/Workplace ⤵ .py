import pickle
import streamlit as st 
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model= pickle.load(open('parkinsons_model.sav','rb'))

# Sidebar for Nevigation
with st.sidebar:
    selected = option_menu("Health Assistant",
                            ["Diabetes Prediction",
                            'Heart Disease Prediction',
                            'Parkinsons Prediction' ],
                            icons = ['activity','heart','person'],default_index = 0)

# Diabetes Prediciton Page
if (selected == 'Diabetes Prediction'):
    #page title 
    st.title("Diabetes prediction with Health Assistant")  
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnencies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Gluecose level")
    with col3:
        BloodPressure = st.text_input("BloodPressure")
    with col1:
        SkinThickness = st.text_input("Skin Thickness")
    with col2:
        Insulin = st.text_input("Insulin")
    with col3:
        BMI = st.text_input("BMI value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    with col2:
        Age = st.text_input("Age of the Person")
    
     # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[ Pregnencies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)

# Heart Disease Prediciton Page
if (selected == 'Heart Disease Prediction'):
    #page title 
    st.title("Heart Disease Prediction with Health Assistant")  
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Please enter your Age")
    with col2:
        sex=st.text_input("Please Choose Gender M=1,F=0")  
    with col3:
        cp = st.text_input("Please enter your Chest pain types")
    with col1:
        trestbps = st.text_input("Please enter Resting Blood Pressure")
    with col2:
        chol = st.text_input("Please enter Serum Cholestroal in mg/dl")
    with col3:
        fbs = st.text_input("Please enter Fasting Blood Sugar>120")
    with col1:
        restecg = st.text_input("Please enter Resting Elctrocardiographic results ")
    with col2:
        thalach = st.text_input("Please enter Maximum Heart rate achived")
    with col3:
        exang = st.text_input("Please enter Excercise Induced Angina")
    with col1:
        oldpeak = st.text_input("Please enter ST depression induced by excercise")
    with col2:
        slope = st.text_input("Please enter slope of the peak exercise ST segment")
    with col3:
        ca = st.text_input("Please enter Major vessels colored by flourosopy")
    with col1:
        thal = st.text_input("Please enter thal:0=normal; 1=fixed defect; 2 = reverseable defect")

 
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[ age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The Pereson having Heart Disease'
        else:
            heart_diagnosis = 'The Pereson does not have any Heart Disease'
        
    st.success(heart_diagnosis)

#  parkinsons Prediciton Page
if (selected == 'Parkinsons Prediction'):
    #page title 
    st.title("Parkinsons Prediction with Health Assistant")  
    
    # getting the input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
    
     # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The Person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The Person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)     
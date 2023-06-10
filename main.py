import numpy as np
import pickle
import streamlit as st

# Loading the trained model
loaded_model = pickle.load(open('C:/Users/othma/Downloads/trained_model.sav', 'rb'))

# A function that predicts if the person is diabetic or not
def diabetes_prediction(input_data):
    y_pred = loaded_model.predict(input_data)
    if y_pred[0] == 1:
        return "This person is diabetic!!"
    else:
        return "This person is not diabetic!!"

# The main function
def main():
    # giving a title to the web application
    st.title('Diabetes Prediction Web App')

    # getting the input data from the user
    Pregnancies = st.text_input('The number of Pregnancies')
    Glucose = st.text_input('The Glucose level')
    BloodPressure = st.text_input('The Blood Pressure value')
    SkinThickness = st.text_input('The Skin Thickness value')
    Insulin = st.text_input('The Insulin level')
    BMI = st.text_input('The BMI value')
    DiabetesPedigreeFunction  = st.text_input('The Diabetes Pedigree Function value')
    Age = st.text_input('The person Age')

    # making a diabetes prediction
    diagnosis = ''
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    st.success(diagnosis)

if __name__ == "__main__":
    main()

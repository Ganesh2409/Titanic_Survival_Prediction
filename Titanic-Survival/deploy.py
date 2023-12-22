import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

def predict():
    st.title("Do They Survive :ship:")

    column_transformer = pickle.load(open('models/column_transformer.pkl', 'rb'))
    standard_scalar = pickle.load(open('models/standard_scaler.pkl', 'rb'))
    model = pickle.load(open('models/classifier.pkl', 'rb'))

    Pclass = st.slider("Select the Pclass of passenger", 1, 4, 0, key="pclass_slider_deploy")
    Sex = st.selectbox("Select the gender of passenger", ['male', 'female'], key="sex_selectbox_deploy")
    Age = st.number_input(" Input Age of the passenger", 0, 100, key="age_input_deploy")
    SibSp = st.slider("Select the SibSp of passenger", 0, 8, 0, key="sibsp_slider_deploy")
    Parch = st.slider("Select the Parch of passenger", 0, 6, 0, key="parch_slider_deploy")
    Fare = st.number_input("Enter the fare charged to travel in the Titanic", 0, 512, key="fare_input_deploy")
    Embarked = st.selectbox("Select the Embarked location", ['S', 'Q', 'C'], key="embarked_selectbox_deploy")

    row = np.array([Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]).reshape(1, 7)

    df = pd.DataFrame(data=row, columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'])

    transformed_df = column_transformer.transform(df)
    scaled_df = standard_scalar.transform(transformed_df)

    ok = st.button('Predict')

    if ok :
        prediction = model.predict(scaled_df)[0]

        if prediction == 1:
            st.success("Hurray! The passenger survived! 🎉")
        else:
            st.error("Oh no! The passenger did not survive. 😢")


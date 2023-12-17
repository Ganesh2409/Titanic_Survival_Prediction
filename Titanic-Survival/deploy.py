import streamlit as st,numpy as np,pandas as pd,pickle
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer 
from sklearn.linear_model import LogisticRegression

column_transformer = pickle.load(open('Titanic-Survival/models/column_transformer.pkl','rb'))
standard_scalar = pickle.load(open('Titanic-Survival/models/standard_scaler.pkl', 'rb'))
model = pickle.load(open('Titanic-Survival/models/classifier.pkl','rb'))

st.title("Do They Survive :ship:")

Pclass = st.select_slider("Input the Pclass of the passenger",[1,2,3,4])
Sex = st.select_slider("Input the Sex pf the passener ",['male','female'])
Age = st.number_input("input the Age of the passenger",0,100)
SibSp = st.select_slider("input the SibSp",[0, 1, 2, 4, 8, 3, 5])
Parch = st.select_slider("select the Parch ",[2, 1, 0, 5, 3, 4, 6])
Fare = st.number_input("enter the fare they cahrged to travell in the Titanic ",0,512)
Embarked = st.select_slider("select the Embarked location",['S','Q','C'])
@st.cache_data
def predict():
     row = np.array([Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]).reshape(1, 7)
     df = pd.DataFrame(data=row, columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'])
     transformed_df = column_transformer.transform(df) 
     scaled_df = standard_scalar.transform(transformed_df)
     prediction = model.predict(scaled_df)[0]


     if prediction == 1:
          st.success("Hurray! The passenger survived! 🎉")
     else:
          st.error("Oh no! The passenger did not survive. 😢")



st.button("Predict", on_click=predict) 




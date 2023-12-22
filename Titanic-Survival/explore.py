import numpy as np
import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt
import warnings 
from sklearn.compose import ColumnTransformer 
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
warnings.filterwarnings('ignore')
import streamlit as st

def filter():
    pass 


def load_data():
    titanic = pd.read_csv('Titanic-Dataset.csv')
    unessential_columns = ["PassengerId","Name","Ticket",'Cabin']
    data = titanic.drop(columns = unessential_columns)
    data = data.dropna()
    return data 


df = load_data()

def show_explore_page():
    st.title('Lets explore the deep trenches of Titanic  :ocean:')
    st.write(' Lets See some Graphs and Plots')

    st.write("### Sex Vs Survived ")
    fig, ax = plt.subplots()
    sns.barplot(x=df['Sex'],y=df['Survived'])
    # Show the plot
    st.pyplot(fig)

    st.write("### Age Vs Fare Vs Sex")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df['Age'], y=df['Fare'], hue=df['Sex'], ax=ax)
    # Show the plot
    st.pyplot(fig)
    
    st.write("### Detect Outliers ")
    fig,ax = plt.subplots()
    sns.boxplot(x=df['Sex'],y=df['Age'],hue = df['Survived'])
    st.pyplot(fig)

    st.write("### Rate of Surival and Death")
    # Create subplots
    fig, ax = plt.subplots()

    # Plot the first distribution
    sns.distplot(df[df['Survived'] == 0]['Age'], hist=False, label='Not Survived', ax=ax)

    # Plot the second distribution
    sns.distplot(df[df['Survived'] == 1]['Age'], hist=False, label='Survived', ax=ax)

    # Show legend
    ax.legend()

    # Show the plot
    st.pyplot(fig)

    





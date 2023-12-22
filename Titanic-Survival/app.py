import streamlit as st
from explore import show_explore_page
from deploy import predict
import warnings


warnings.filterwarnings('ignore')

def main():
    page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))
    
    if page == "Predict":
        predict()
    else:
        show_explore_page()

if __name__ == "__main__":
    main()

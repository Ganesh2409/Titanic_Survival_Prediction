
# ⚓ Titanic Survival Prediction App 
### Let's See --> [Who Can Make It ](https://ganesh2409-titanic-survival-prediction.streamlit.app/) ![Predict](https://img.shields.io/badge/Streamlit-indigo) 


This project is a Streamlit-based web application that predicts whether a passenger would survive the Titanic disaster based on various input features. The app allows users to explore the Titanic dataset and make predictions using a trained machine learning model.

##  📁 Project Structure

- **`app.py`**: The main file that runs the Streamlit app. It includes options to either explore the dataset or make survival predictions.
- **`deploy.py`**: Handles the prediction functionality. Loads the pre-trained machine learning model and processes user inputs to predict the survival of a Titanic passenger.
- **`explore.py`**: Contains the code to visualize various aspects of the Titanic dataset, providing insights into factors that influenced survival rates.
- **`Titanic_Survival.ipynb`**: A Jupyter Notebook containing the steps involved in data cleaning, exploration, feature engineering, and model training.
- **`models/`**: A directory where the pre-trained models and transformers are stored for making predictions.
  - `column_transformer.pkl`: The ColumnTransformer used for processing the dataset.
  - `standard_scaler.pkl`: The StandardScaler used to standardize the features.
  - `classifier.pkl`: The Logistic Regression model trained to predict survival.

## 🛠️ How to Run the App

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ganesh2409/Titanic_Survival_Prediction.git
   cd Titanic_Survival_Prediction
   ```

2. **Install Dependencies**:
   Make sure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**:
   To start the Streamlit app, run the following command:
   ```bash
   streamlit run app.py
   ```

4. **Interact with the App**:
   - Navigate to the "Explore" page to visualize the dataset.
   - Use the "Predict" page to input passenger details and predict their survival.

## 📄 Dataset

The dataset used in this project is the famous Titanic dataset, which contains information about the passengers aboard the Titanic. Key features include:

- **Pclass**: Passenger class (1st, 2nd, 3rd)
- **Sex**: Gender of the passenger
- **Age**: Age of the passenger
- **SibSp**: Number of siblings/spouses aboard the Titanic
- **Parch**: Number of parents/children aboard the Titanic
- **Fare**: Fare paid for the ticket
- **Embarked**: Port of Embarkation (C=Cherbourg; Q=Queenstown; S=Southampton)

## 🚀 Model

The model used in this project is a Logistic Regression model trained on the processed Titanic dataset. The pipeline involves:

1. **Data Cleaning**: Handling missing values, dropping unnecessary columns.
2. **Feature Engineering**: Applying transformations to categorical and numerical features.
3. **Model Training**: Training a Logistic Regression model using Scikit-learn.

## Results

The model achieves a reasonable accuracy on the test set, and the app provides users with real-time predictions based on their input.

##  🖥️ Future Improvements

- Enhance the model's accuracy by experimenting with other algorithms like RandomForest or XGBoost.
- Incorporate additional data preprocessing steps to handle outliers and imbalanced data.
- Deploy the app on a cloud platform for wider accessibility.


##  🤝 Contact
For any questions or feedback, please co ntact:
- **Name** - [Ganesh Chowdhary P]()
- **Email** - [pinnamaneniganesh24@gmail.com ](mailto:your.pinnamaneniganesh24@gmail.com)
  
Made with ❤️ ( ͡• ͜ʖ ͡• ) Follow for more  ... :) 

# California Housing Price Prediction

A machine learning regression project that predicts the median house value of a district in California using the California Housing dataset. The project covers the complete machine learning workflow, including data preprocessing, feature engineering, model training, hyperparameter tuning, model serialization, and deployment with Streamlit.

---

## 🚀 Live Demo

👉 **[Launch the Application](https://california-regression-amina.streamlit.app)**

---

## Project Overview

This project aims to build a regression model capable of predicting the median house value of a California district based on various housing and demographic features.

The project demonstrates a complete end-to-end machine learning pipeline:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model training
- Hyperparameter tuning
- Model evaluation
- Model serialization
- Streamlit deployment

---

## Dataset

The project uses the **California Housing Dataset**, which contains information about California districts such as:

- Longitude
- Latitude
- Housing Median Age
- Total Rooms
- Total Bedrooms
- Population
- Households
- Median Income

**Target Variable**

- Median House Value

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Joblib

---

## Project Workflow

```
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Exploratory Data Analysis
   │
   ▼
Feature Engineering
   │
   ▼
Model Training
   │
   ▼
Hyperparameter Tuning
   │
   ▼
Model Evaluation
   │
   ▼
Model Serialization
   │
   ▼
Streamlit Deployment
```

---

## Exploratory Data Analysis (EDA)

The following preprocessing steps were performed:

- Checked for missing values
- Missing values accounted for less than 1% of the dataset
- Missing rows were removed
- Explored feature distributions
- Examined feature relationships
- Prepared the dataset for model training

---

## Feature Engineering

The following engineered features were created:

- Room per House
- Beds per Room
- Bedroom per House

These engineered features were added to improve the predictive performance of the regression model.

---

## Models Trained

Multiple regression algorithms were trained and evaluated.

The best-performing model was selected after comparing evaluation metrics.

---

## Hyperparameter Tuning

Hyperparameter tuning was performed using:

- RandomizedSearchCV
- GridSearchCV (Fine Tuning)

The best parameters obtained were used to train the final Random Forest Regression model.

---

## Model Evaluation

The trained models were evaluated using regression metrics such as:

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

The final model was selected based on its overall performance.

---

## Model Comparison

| Model                  |  Train_R2 |   Test_R2 | MAE_Train |  MAE_Test | RMSE_Train | RMSE_Test |
| ---------------------- | --------: | --------: | --------: | --------: | ---------: | --------: |
| LinearRegression       |     0.430 |     0.390 |     50830 |     50733 |      69651 |     69228 |
| LinearRegression+FE    |     0.460 |     0.415 |     49789 |     49690 |      68665 |     68212 |
| DecisionTree           |     1.000 |     0.600 |         0 |     46259 |          0 |     71293 |
| DecisionTree Tuned     |     0.829 |     0.653 |     29106 |     41153 |      44264 |     61819 |
| RandomForest           |     0.968 |     0.725 |     12561 |     34205 |      19189 |     51334 |
| **RandomForest Tuned** | **0.955** | **0.765** | **13444** | **31735** |  **22744** | **48897** |

---

## Model Serialization

The final trained model was serialized using **Joblib**.

This allows the trained model to be loaded directly into the Streamlit application without retraining.

---

## Deployment

A user-friendly web application was developed using **Streamlit**.

The application allows users to:

- Enter housing details
- Predict the estimated house price
- View the prediction instantly

---

## ▶ Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Amina0426/california_regression.git
```

### 2. Navigate to the project directory

```bash
cd california_regression
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open automatically in your web browser.

---

## Project Structure

```
├── data/
├── models/
├── requirements.txt
├── notebooks/
├── README.md
└── apps.py
```

---

## Learning Outcomes

Through this project, the following concepts were implemented:

- Data preprocessing
- Handling missing values
- Feature engineering
- Regression modeling
- Model evaluation
- Hyperparameter tuning
- Model serialization
- Streamlit deployment

---

## Future Improvements

Possible future enhancements include:

- Improve prediction accuracy using advanced boosting algorithms
- Deploy the application to Streamlit Community Cloud
- Add interactive visualizations
- Improve the user interface
- Perform automated feature selection
- Add model explainability using SHAP or LIME

---

## Author

**Amina**

Machine Learning | Data Structures and Algorithms | Python | Web Development

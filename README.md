
# major-project-unlox
 Streamlit url : https://sreamlitproject-jrcazsyss7sasvjevtxcnp.streamlit.app/
 # Used Car Price Prediction

## Project Overview

The **Used Car Price Prediction** project is a machine learning application that predicts the estimated selling price of a used car based on important vehicle characteristics.

The project includes data preprocessing, exploratory data analysis, feature engineering, machine learning model training, model evaluation, and deployment using **Streamlit**.

The final application provides an easy-to-use interface where users can enter car details and receive an estimated price instantly.

## Problem Statement

Determining the appropriate price of a used car can be difficult because the price depends on several factors such as the car's brand, model, manufacturing year, kilometers driven, fuel type, transmission type, and other vehicle specifications.

This project aims to build a machine learning model that can learn patterns from historical car data and predict the expected price of a used car.

## Objectives

* Analyze and preprocess used car data.
* Identify important factors affecting car prices.
* Perform exploratory data analysis.
* Prepare the dataset for machine learning.
* Train and evaluate machine learning models.
* Select a suitable model for price prediction.
* Build an interactive Streamlit application.
* Deploy the application for real-world use.

## Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **Streamlit**
* **Pickle**
* **Jupyter Notebook**
* **Git & GitHub**

## Machine Learning Workflow

The project follows these major steps:

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Data Preprocessing
5. Feature Engineering
6. Feature Selection
7. Model Training
8. Model Evaluation
9. Model Serialization
10. Streamlit Application Development
11. Deployment

## Input Features

The Streamlit application accepts relevant car details such as:

* Car brand/company
* Car model
* Manufacturing year
* Kilometers driven
* Fuel type
* Transmission type
* Engine
* Mileage
* Power
* Number of seats
* Other relevant vehicle features

The exact input fields depend on the features used during model training.

## Model

Multiple machine learning approaches can be evaluated during the model-building process. The best-performing model is selected based on appropriate regression evaluation metrics.

Common evaluation metrics include:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

The selected trained model is saved using a serialized model/pipeline file and loaded by the Streamlit application for making predictions.

## Streamlit Application

The trained model is integrated into a Streamlit web application.

Users can:

1. Enter the required car information.
2. Submit the details.
3. Get the predicted used-car price.
4. Interact with the model through a simple web interface.

## Project Structure

```text
used_car_price_prediction/
│
├── app.py
├── model_pipeline.pkl
├── requirements.txt
├── README.md
│
├── dataset/
│   └── used_car_data.csv
│
├── notebooks/
│   └── used_car_price_prediction.ipynb
│
└── images/
    └── app_screenshot.png
```

> The actual folder and file names may vary depending on your project structure.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the Project Folder

```bash
cd used_car_price_prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

## Deployment

The application is deployed using **Streamlit Community Cloud**.

The deployment process involves:

* Uploading the project to GitHub.
* Adding `app.py`.
* Adding the trained model/pipeline file.
* Adding `requirements.txt`.
* Connecting the GitHub repository to Streamlit.
* Selecting `app.py` as the main application file.
* Deploying the application.

## Example Prediction

After entering the required vehicle details, the application generates an estimated used-car price based on the trained machine learning model.

## Results

The project demonstrates how machine learning can be used to estimate used-car prices from historical vehicle data.

The Streamlit deployment makes the trained model accessible through an interactive web application without requiring users to run the machine learning code manually.

## Future Improvements

* Improve prediction accuracy with additional data.
* Experiment with advanced regression algorithms.
* Add more vehicle features.
* Improve the user interface.
* Add data visualizations to the Streamlit application.
* Provide price comparison and market insights.
* Continuously retrain the model using updated used-car data.

## Conclusion

The **Used Car Price Prediction** project combines data analysis, machine learning, and web deployment to create a practical application for estimating used-car prices. The project demonstrates the complete machine learning workflow, from data preprocessing and model development to deployment through Streamlit.

## Author

**Somya Gupta**

Computer Science and Business System
Data Analytics & Machine Learning Project


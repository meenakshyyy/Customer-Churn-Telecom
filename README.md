# Customer-Churn-Telecom

[Customer Churn Deployment ](https://customer-churn-telecom-app.streamlit.app/)

## Project Overview
This project is a **machine learning-based solution** designed to predict customer churn in the **telecom industry**. By analyzing various customer attributes, such as **services subscribed, account details, and demographics**, the model helps identify customers at risk of leaving. The goal is to enable telecom companies to take proactive retention measures, improving customer satisfaction and reducing revenue loss.  

This Project involves collecting and preprocessing data, conducting exploratory data analysis (EDA), and engineering features that capture key customer behaviors such as usage patterns, billing trends, and customer support interactions. A range of classification algorithms, including Logistic Regression, Random Forest, and XGBoost, are evaluated for their predictive performance using metrics and performing deployment using streamlit.

---

## Dataset
The dataset used in this project was obtained from **Kaggle**:
**Dataset Link:** [Telco Customer Churn - Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

### Dataset Description
The dataset contains information about **7,043 telecom customers**, covering various aspects such as services used, billing details, and demographic information. The **target variable** is **Churn**, indicating whether a customer left the telecom service.

### Key Features
1. **Churn Status:**
   - Identifies whether a customer has churned (`Yes` or `No`).
2. **Services Signed Up:**
   - Phone Service, Multiple Lines, Internet Service, Online Security, Online Backup, Device Protection, Tech Support, Streaming TV & Movies.
3. **Account Information:**
   - Customer tenure (how long they've been a customer), contract type, payment method, paperless billing, monthly charges, and total charges.
4. **Demographic Information:**
   - Gender, age range, presence of partners and dependents.

This dataset is useful for analyzing **customer retention trends** and developing strategies to minimize churn.

---

## Technologies Used
The project is implemented using **Python** and leverages the following libraries and frameworks:

### Programming & Development
- **Python** – Core programming language
- **Jupyter Notebook** – For data exploration and model development
- **Streamlit** – For creating an interactive web-based app

### Data Processing & Machine Learning
- **Pandas** – Data manipulation and preprocessing
- **NumPy** – Numerical computations
- **Scikit-Learn (sklearn)** – Machine learning algorithms and evaluation metrics

### Data Visualization
- **Seaborn** – Statistical visualizations
- **Matplotlib** – Basic plots and charts

---

## Installation & Setup Guide

### 1️⃣ Clone the Repository
First, clone the GitHub repository to your local system using:
```bash
git clone https://github.com/meenakshyyy/Customer-Churn-Telecom.git
cd customer-churn-prediction
```

### 2️⃣ Install Dependencies
Ensure you have **Python 3.x** installed, then install all required libraries from `requirements.txt`:
```bash
pip install -r requirements.txt
```

Alternatively, you can manually install the core dependencies:
```bash
pip install pandas numpy scikit-learn seaborn matplotlib streamlit
```

### 3️⃣ Running the Jupyter Notebook
If you want to explore the dataset and train models interactively, launch Jupyter Notebook:
```bash
jupyter notebook
```
Then, open the notebook file (`customer_churn_analysis.ipynb`) and run the cells step by step.

### 4️⃣ Running the Streamlit Web App
If the project includes a **Streamlit-based web app**, you can launch it using:
```bash
streamlit run app_model.py
```
This will start a web-based interface where you can **upload new customer data** and get churn predictions.

---

## Model Performance & Results
We tested multiple machine learning models for churn prediction, and the results are as follows:

- **Logistic Regression**: 79% accuracy
- **Decision Tree**: 79% accuracy
- **Random Forest**: 79% accuracy
- **XGBoost**: 80% accuracy
- **Hyperparameter Tuned XGBoost**: 79% accuracy

With further training and processing, the model can achieve even better performance.


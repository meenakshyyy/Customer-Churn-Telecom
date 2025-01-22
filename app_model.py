import streamlit as st
import pandas as pd
import pickle

# Load the Random Forest model from the pickle file
model_file_path=model.pkl
with open(model_file_path, 'rb') as model_file:
    model = pickle.load(model_file)

columns =["Gender", "SeniorCitizen","Partner","Dependents","PhoneService","MultipleLines", "InternetServiceType", "OnlineSecurity", "OnlineBackup", 
                         "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies", "ContractType",  "PaperlessBilling",
                         "PaymentMethod","Tenure","MonthlyCharges","TotalCharges"]

# Create a function to preprocess user input and make predictions


def predict_churn(input_data):
    # Preprocess the input data
    input_df = pd.DataFrame([input_data], columns=columns)

    # Make predictions using the loaded model
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[:, 1]

    return prediction[0],probability[0]


# Create the Streamlit app


def main():
    st.title("Telecom Churn Prediction")
    st.write("Enter the customer details below to predict churn.")

    # Create input fields for user input
    tenure = st.number_input("Tenure (months)")
    phone_service = st.selectbox("Phone Service", ["No","Yes","No phone service"])
    contract = st.selectbox("Contract",["One year" ,"Two year" ,"Month-to-month"] )
    paperless_billing = st.selectbox("Paperless Billing", ["No"," Yes"])
    payment_method = st.selectbox("Payment Method", [ "Bank transfer (automatic)", "Credit card (automatic)", "Electronic check","Mailed check"])
    monthly_charges = st.number_input("Monthly Charges")
    device_protection = st.selectbox("Device Protection", ["Yes", "No","No internet service"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No","No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["Yes", "No","No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No","No internet service"])
    

    gender = st.selectbox("Gender", ["Male", "Female"])
    st.write("Select the gender of the customer")

    senior_citizen = st.selectbox("Senior Citizen", [0, 1])

    partner = st.selectbox("Partner",["Yes", "No"] )
    dependents = st.selectbox("Dependents", ["Yes", "No"])

    multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No","No internet service"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No internet service"])
    online_security = st.selectbox("Online Security", ["Yes", "No","No internet service"])
    online_backup = st.selectbox("Online Backup", ["Yes", "No","No internet service"])
    total_charges=st.number_input("Total Charges")
    # Create a dictionary to store the user input
    input_data = {
        'Gender': gender,
        'SeniorCitizen': senior_citizen,
        'Partner': partner,
        'Dependents': dependents,
        'PhoneService': phone_service,
        'MultipleLines': multiple_lines,
        'InternetServiceType': internet_service,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'ContractType': contract,
        'PaperlessBilling': paperless_billing,
        'PaymentMethod': payment_method,
        'Tenure':tenure,
        'MonthlyCharges':monthly_charges,
        'TotalCharges':total_charges
}
    
    # Predict churn based on user input
    churn_probability = predict_churn(input_data)
    churn_prediction=churn_probability[1]
    # Display the prediction
    st.subheader("Churn Prediction")
    if churn_prediction >= 0.4:
        st.write("The customer is likely to churn.")
    else:
        st.write("The customer is unlikely to churn.")

    # Display the churn probability
    st.subheader("Churn Probability")

    st.write("The probability of churn is:", churn_probability)


# Run the Streamlit app
if __name__ == '__main__':
    main()

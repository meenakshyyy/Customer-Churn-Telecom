import pickle
import streamlit as st

model=pickle.load(open('model.pkl','rb'))
encoded_feature=pickle.load(open('onehot_enc.pkl','rb'))
#encode_target=pickle.load(open('label_enc.pkl','rb'))
scaler=pickle.load(open("Scaled.pkl",'rb'))

def main():
    st.title("Churn Prediction")
#input variables
    with st.form("my_form"):
        Gender=st.selectbox("Gender",("Male","Female"),index=None,placeholder='Enter your input')
        SeniorCitizen=st.selectbox("Senior Citizen",("Yes","No"),index=None,placeholder='Enter your input')
        Partner=st.selectbox("Partner",("Yes","No"),index=None,placeholder='Enter your input')
        Dependents=st.selectbox("Dependents",("Yes","No"),index=None,placeholder='Enter your input')
        Tenure=st.number_input("Tenure",placeholder="Enter your input")
        PhoneService=st.selectbox("Phone Service",("Yes","No"),index=None,placeholder='Enter your input')
        MultipleLines=st.selectbox("Multiple Lines",("Yes","No","No phone service"),index=None,placeholder='Enter your input')
        InternetService=st.selectbox("Internet Service",("DSL","Fiber optic","No"),index=None,placeholder='Enter your input')
        OnlineSecurity=st.selectbox("Online Security",("Yes","No","No internet service"),index=None,placeholder='Enter your input')
        OnlineBackup=st.selectbox("Online Backup",("Yes","No","No internet service"),index=None,placeholder='Enter your input')
        DeviceProtection=st.selectbox("Device Protection",("Yes","No","No internet service"),index=None,placeholder='Enter your input')
        TechSupport=st.selectbox("Tech Support",("Yes","No","No internet service"),index=None,placeholder='Enter your input')
        StreamingTV=st.selectbox("Stream TV",("Yes","No","No internet service"),index=None,placeholder='Enter your input')
        StreamingMovies=st.selectbox("Stream Movies",("Yes","No","No internet service"),index=None,placeholder='Enter your input')
        Contract=st.selectbox("Contract",("One year","Month-to-month","Two year"),index=None,placeholder='Enter your input')
        PaperlessBilling=st.selectbox("Paperless Billing",("Yes","No"),index=None,placeholder='Enter your input')
        PaymentMethod=st.selectbox("Payment Method",("Mailed check","Bank transfer (automatic)","Electronic check"),index=None,placeholder='Enter your input')
        MonthlyCharges=st.number_input("Monthly Charges",placeholder='Enter your input')
        TotalCharges=st.number_input("Total Charges",placeholder='Enter your input')
       # button=st.form_submit_button("Predict")

        if st.form_submit_button("Predict"):
            encoded_output=[scaler.transform([[TotalCharges]])]
            st.write(encoded_output)
            
if __name__=="__main__":
    main()
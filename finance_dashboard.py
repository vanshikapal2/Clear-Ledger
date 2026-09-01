import streamlit as st
import pandas as pd
import joblib

# === Load the trained model and feature names ===
model = joblib.load('C:\\Users\\Dhusyath\\Downloads\\PROJECTS_DA\\PROJECTS_DA\\Finance & Banking\\loan_risk_model.pkl')
feature_names = joblib.load('C:\\Users\\Dhusyath\\Downloads\\PROJECTS_DA\\PROJECTS_DA\\Finance & Banking\\model_features.pkl')

st.set_page_config(
    page_title="ClearLedger",
    page_icon="assets/favicon.svg",
    layout="centered",
)

st.markdown(
    """
    <style>
        .block-container { padding-top: 2rem; }
        .cl-header { margin-bottom: 1.5rem; }
        .cl-tagline {
            color: #64748B;
            font-size: 0.95rem;
            margin-top: 0.25rem;
        }
        .cl-result {
            border: 1px solid #E2E8F0;
            border-radius: 6px;
            padding: 1rem 1.25rem;
            margin-top: 0.5rem;
            background: #FFFFFF;
        }
        .cl-result-low { border-left: 3px solid #059669; }
        .cl-result-high { border-left: 3px solid #DC2626; }
        .cl-result-label {
            font-weight: 600;
            color: #18181B;
            margin: 0;
        }
        div[data-testid="stForm"] label { color: #64748B; }
    </style>
    """,
    unsafe_allow_html=True,
)

col_logo, col_tag = st.columns([2, 3])
with col_logo:
    st.image("assets/logo.svg", width=160)
with col_tag:
    st.markdown(
        '<p class="cl-tagline">Loan risk intelligence</p>',
        unsafe_allow_html=True,
    )

st.markdown("Provide customer loan application details below.")

# === User Input Form ===
with st.form("loan_form"):
    loan_amount = st.number_input("Loan Amount", min_value=0)
    annual_income = st.number_input("Annual Income", min_value=0)
    annual_expenses = st.number_input("Annual Expenses", min_value=0)
    credit_score = st.slider("Credit Score", 300, 850, 600)

    approval_channel = st.selectbox("Approval Channel", ["Branch", "Online"])
    approval_status = st.selectbox("Approval Status", ["Approved", "Rejected"])
    co_applicant = st.selectbox("Co-Applicant Present", ["Yes", "No"])

    submitted = st.form_submit_button("Assess risk")

if submitted:
    # === Prepare input dictionary ===
    input_dict = {
        "Loan_Amount": loan_amount,
        "Annual_Income": annual_income,
        "Annual_Expenses": annual_expenses,
        "Credit_Score": credit_score,
        f"Approval_Channel_{approval_channel}": 1,
        f"Approval_Status_{approval_status}": 1,
        f"Co_Applicant_{co_applicant}": 1
    }

    # === Convert to DataFrame and encode ===
    input_df = pd.DataFrame([input_dict])
    input_df_encoded = pd.get_dummies(input_df)
    input_df_encoded = input_df_encoded.reindex(columns=feature_names, fill_value=0)

    # === Make Prediction ===
    prediction = model.predict(input_df_encoded)[0]
    is_default = prediction == 1
    result_class = "cl-result-high" if is_default else "cl-result-low"
    result_label = "Default risk detected" if is_default else "Low default risk"

    st.subheader("Prediction Result")
    st.markdown(
        f'<div class="cl-result {result_class}">'
        f'<p class="cl-result-label">{result_label}</p>'
        f'</div>',
        unsafe_allow_html=True,
    )

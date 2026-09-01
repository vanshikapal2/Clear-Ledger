# ClearLedger

Loan risk intelligence — a predictive analytics platform for assessing loan default risk across diverse customer segments. Built on **1,000,000+ loan applications** to help financial institutions make data-driven credit decisions.

---

## GitHub Project Repository

[View ClearLedger on GitHub](https://github.com/vanshikapal2/Clear-Ledger-)

---

## Project Overview

Loan defaults pose a significant challenge to financial stability and lending efficiency. ClearLedger delivers an end-to-end analytics platform that enables:

- Risk profiling of loan applicants
- Portfolio-level default trend analysis
- Predictive modeling for credit decisions
- Dashboard-driven insights for compliance and strategy

---

## Key Objectives

- Clean and preprocess large-scale loan application data
- Engineer features for default prediction and dashboarding
- Build classification models to assess loan risk
- Deploy interactive dashboards for stakeholder decision-making

---

## Project Structure

| File Name | Description |
|-----------|-------------|
| `loan Default risk managemnt cleaned.csv` | Alternate cleaned dataset version |
| `cleaned_loandefault.csv` | Preprocessed dataset with feature engineering |
| `loan_risk_model.pkl` | Trained model for predicting loan default |
| `model_features.pkl` | Feature list used in model training |
| `loandefault.sql` | SQL queries for data extraction and filtering |
| `sqlconnect.py` | Python script for SQL database connection |
| `app.py` | Flask API for risk prediction |
| `finance_dashboard.py` | Streamlit dashboard for real-time risk assessment |
| `test_request.py` | Script for model testing and API simulation |
| `Loan Default Risk Management System.ipynb` | Jupyter notebook with EDA, modeling, and insights |
| `assets/logo.svg` | ClearLedger logo |
| `assets/favicon.svg` | Browser favicon |
| `.streamlit/config.toml` | Streamlit theme configuration |

---

## Data Preprocessing

- Converted `Application_Date` to datetime format
- Calculated `Debt_to_Income` and `Income_Loan_Ratio`
- Imputed missing values in `Property_Ownership`
- One-hot encoded categorical features (`Employment_Status`, `Region`, `Loan_Purpose`)
- Removed outliers and normalized financial metrics

---

## Exploratory Data Analysis

- Default trends by region, credit score, and loan purpose
- Income vs. loan amount correlation
- Approval channel impact on default rates
- Distribution of monthly installments and loan terms

---

## Modeling Approach

- **Target Variable**: `Defaulted`
- **Algorithms Used**: Logistic Regression, Random Forest, XGBoost
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1 Score, ROC-AUC
- **Top Features**: `Credit_Score`, `Debt_to_Income`, `Past_Defaults`, `Loan_Amount`

---

## Dashboard Overview

### Power BI Dashboard

Visualizes credit risk and portfolio health:

- Regional default heatmaps
- Credit score and income distribution
- Application timeline analysis
- KPI cards for approval rates, risk levels, and loan volumes

![Power BI Preview](https://image2url.com/images/1755871634591-7a6738ed-73b7-447c-8d03-3755af64f941.png)
![Power BI Preview](https://image2url.com/images/1755871674837-e5dee7d7-0703-4518-98a1-625d7fe1b1c9.png)
![Power BI Preview](https://image2url.com/images/1755871704889-969bdcfe-eca6-4c51-a398-d17c87fd727e.png)

---

### ClearLedger Streamlit App

Interactive dashboard for real-time risk prediction:

- Customer-level risk summary
- Default prediction tool
- Feature importance visualization
- Filters by region, employment status, and loan purpose

![Streamlit Preview](https://image2url.com/images/1755871719986-655e09b3-c276-4f1e-93c4-b128727f7ad0.png)
![Streamlit Preview](https://image2url.com/images/1755871736248-a4345b92-7469-4c8c-ae9f-ab750bb025a8.png)

---

## Deployment

- Model serialized with `joblib` as `loan_risk_model.pkl`
- Dashboard deployed via **Streamlit Cloud**
- SQL integration for dynamic data updates
- Git LFS used for large file management

---

## Business Impact

- Flags high-risk applicants before loan approval
- Improves portfolio health and reduces NPA rates
- Enables real-time credit risk monitoring
- Supports data-driven lending strategy and compliance

---

## Tech Stack

- **Python**: Pandas, NumPy, Scikit-learn, Streamlit, Flask
- **SQL**: Data extraction and filtering
- **Visualization**: Power BI, Matplotlib, Seaborn, Plotly
- **Deployment**: Streamlit Cloud, GitHub, Git LFS

---

## Future Enhancements

- Integrate real-time credit bureau APIs
- Add explainability via SHAP or LIME
- Enable user-uploaded loan applications for prediction
- Expand dashboard to include repayment forecasting and risk scoring

---

## Author

**Anesh Raj**

[GitHub Profile](https://github.com/aneshraj-d96)

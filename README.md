# ClearLedger

Predictive analytics platform for loan default risk, built on 1M+ loan applications to support data-driven credit decisions.

**[GitHub Repo](https://github.com/vanshikapal2/Clear-Ledger-)**

## Overview
End-to-end platform for risk profiling, portfolio trend analysis, predictive credit modeling, and compliance dashboards.

## Approach
- **Data**: Cleaned 1M+ records; engineered features like `Debt_to_Income`, `Income_Loan_Ratio`; encoded categorical fields (Employment, Region, Loan Purpose)
- **Modeling**: Logistic Regression, Random Forest, XGBoost — evaluated via Accuracy, Precision, Recall, F1, ROC-AUC. Top features: `Credit_Score`, `Debt_to_Income`, `Past_Defaults`, `Loan_Amount`
- **Dashboards**: Power BI (regional heatmaps, KPIs) + Streamlit app (real-time risk prediction, filters, feature importance)

## Tech Stack
Python (Pandas, Scikit-learn, Streamlit, Flask) · SQL · Power BI/Plotly · Streamlit Cloud + Git LFS

## Impact
Flags high-risk applicants pre-approval, improves portfolio health, reduces NPA rates, enables real-time monitoring.

## Roadmap
Real-time credit bureau APIs · SHAP/LIME explainability · user-uploaded predictions · repayment forecasting

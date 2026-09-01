import pandas as pd
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root_",
    database="projects"
)

cursor = conn.cursor()

# Load CSV
df = pd.read_csv("cleaned_loandefault.csv")  # Ensure this file exists in your working directory

# Convert Application_Date to datetime format
df['Application_Date'] = pd.to_datetime(df['Application_Date'], errors='coerce')

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS loan_applications (
        Customer_ID BIGINT,
        Age INT,
        Income BIGINT,
        Annual_Expenses BIGINT,
        Loan_Amount BIGINT,
        Loan_Term_Months INT,
        Credit_Score INT,
        Employment_Status VARCHAR(100),
        Marital_Status VARCHAR(50),
        Education_Level VARCHAR(100),
        Property_Ownership VARCHAR(100),
        Loan_Purpose VARCHAR(100),
        Co_Applicant VARCHAR(100),
        Approval_Channel VARCHAR(100),
        Region VARCHAR(100),
        Application_Date DATETIME,
        Past_Defaults INT,
        Approval_Status VARCHAR(50),
        Defaulted INT
    )
""")

# Insert data row by row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO loan_applications (
            Customer_ID, Age, Income, Annual_Expenses, Loan_Amount,
            Loan_Term_Months, Credit_Score, Employment_Status, Marital_Status,
            Education_Level, Property_Ownership, Loan_Purpose, Co_Applicant,
            Approval_Channel, Region, Application_Date, Past_Defaults,
            Approval_Status, Defaulted
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        int(row['Customer_ID']),
        int(row['Age']),
        int(row['Income']),
        int(row['Annual_Expenses']),
        int(row['Loan_Amount']),
        int(row['Loan_Term_Months']),
        int(row['Credit_Score']),
        row['Employment_Status'],
        row['Marital_Status'],
        row['Education_Level'],
        row['Property_Ownership'] if pd.notnull(row['Property_Ownership']) else None,
        row['Loan_Purpose'],
        row['Co_Applicant'],
        row['Approval_Channel'],
        row['Region'],
        row['Application_Date'].to_pydatetime() if pd.notnull(row['Application_Date']) else None,
        int(row['Past_Defaults']),
        row['Approval_Status'],
        int(row['Defaulted'])
    ))

# Commit and close
conn.commit()
print(" Loan application data imported successfully into MySQL!")
conn.close()

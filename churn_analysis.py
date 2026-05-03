import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, roc_auc_score

df = pd.read_csv(r'C:\Users\Raiqis\OneDrive\Desktop\My_Work\Project_3\Raw_Data\WA_Fn-UseC_-Telco-Customer-Churn.csv')

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'].str.strip(), errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(0)
df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})
df['Churn_Binary'] = df['Churn'].map({'Yes': 1, 'No': 0})

def tenure_group(tenure):
    if tenure <= 12:
        return '0-1 Year'
    elif tenure <= 24:
        return '1-2 Years'
    elif tenure <= 48:
        return '2-4 Years'
    else:
        return '4+ Years'

df['TenureGroup'] = df['tenure'].apply(tenure_group)
df['ChargeTier'] = pd.cut(df['MonthlyCharges'], bins=[0, 35, 65, 95, 999],
                           labels=['Low', 'Medium', 'High', 'Premium'])

service_cols = ['PhoneService', 'OnlineSecurity', 'OnlineBackup',
                'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
df['NumServices'] = df[service_cols].apply(
    lambda row: sum(1 for v in row if v == 'Yes'), axis=1
)

cat_cols = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
            'PhoneService', 'MultipleLines', 'InternetService',
            'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
            'TechSupport', 'StreamingTV', 'StreamingMovies',
            'Contract', 'PaperlessBilling', 'PaymentMethod',
            'TenureGroup', 'ChargeTier']

num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges', 'NumServices']

df_model = df.copy()
le = LabelEncoder()
for col in cat_cols:
    df_model[col] = le.fit_transform(df_model[col].astype(str))

X = df_model[cat_cols + num_cols]
y = df_model['Churn_Binary']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print(classification_report(y_test, y_pred))
print(f"ROC-AUC Score: {roc_auc_score(y_test, y_prob):.4f}")

df['ChurnProbability'] = model.predict_proba(X)[:, 1]
df['ChurnProbability_Pct'] = (df['ChurnProbability'] * 100).round(1)
df['RiskSegment'] = pd.cut(df['ChurnProbability'],
                            bins=[0, 0.33, 0.66, 1.0],
                            labels=['Low Risk', 'Medium Risk', 'High Risk'])

df = df.rename(columns={
    'customerID': 'Customer_ID',
    'gender': 'Gender',
    'SeniorCitizen': 'Senior_Citizen',
    'tenure': 'Tenure',
    'TenureGroup': 'Tenure_Group',
    'PaymentMethod': 'Payment_Method',
    'PaperlessBilling': 'Paperless_Billing',
    'InternetService': 'Internet_Service',
    'PhoneService': 'Phone_Service',
    'MultipleLines': 'Multiple_Lines',
    'OnlineSecurity': 'Online_Security',
    'OnlineBackup': 'Online_Backup',
    'DeviceProtection': 'Device_Protection',
    'TechSupport': 'Tech_Support',
    'StreamingTV': 'Streaming_TV',
    'StreamingMovies': 'Streaming_Movies',
    'MonthlyCharges': 'Monthly_Charges',
    'TotalCharges': 'Total_Charges',
    'ChargeTier': 'Charge_Tier',
    'NumServices': 'Num_Services',
    'Churn_Binary': 'Churn_Binary',
    'ChurnProbability_Pct': 'Churn_Probability_Pct',
    'RiskSegment': 'Risk_Segment'
})

export_cols = [
    'Customer_ID', 'Gender', 'Senior_Citizen', 'Partner', 'Dependents',
    'Tenure', 'Tenure_Group', 'Contract', 'Payment_Method', 'Paperless_Billing',
    'Internet_Service', 'Phone_Service', 'Multiple_Lines',
    'Online_Security', 'Online_Backup', 'Device_Protection',
    'Tech_Support', 'Streaming_TV', 'Streaming_Movies',
    'Monthly_Charges', 'Total_Charges', 'Charge_Tier', 'Num_Services',
    'Churn', 'Churn_Binary', 'Churn_Probability_Pct', 'Risk_Segment'
]

output_dir = r'C:\Users\Raiqis\OneDrive\Desktop\My_Work\Project_3\outputs'
os.makedirs(output_dir, exist_ok=True)

writer = pd.ExcelWriter(rf'{output_dir}\telco_churn_clean.xlsx', engine='openpyxl')
df[export_cols].to_excel(writer, index=False, sheet_name='Churn Data')

worksheet = writer.sheets['Churn Data']
for col in worksheet.columns:
    max_length = max(len(str(cell.value)) for cell in col if cell.value)
    worksheet.column_dimensions[col[0].column_letter].width = max_length + 2

writer.close()
print("Exported: telco_churn_clean.xlsx")

import pandas as pd
import sqlite3

df = pd.read_excel(r'C:\Users\Raiqis\OneDrive\Desktop\My_Work\Project_3\outputs\telco_churn_clean.xlsx')

conn = sqlite3.connect(r'C:\Users\Raiqis\OneDrive\Desktop\My_Work\Project_3\telco_churn.db')

df.to_sql('customers', conn, if_exists='replace', index=False)

print(f"Loaded {len(df)} rows into telco_churn.db")

conn.close()

# Customer-Churn-Analysis
Predicting customer churn using Python, Pandas, SQL, and Tableau

## Key Findings
![Contract](./png/Contract_Graph.png)

Customers churn month to month at over 40% while 2 year contract customers churn at a mere 2.8%. This is the biggest churn driver in the dataset. There's no reason for customers without a long-term commitment to stick around. The company should try to encourage month-to-month customers to sign up for longer term contracts, perhaps with incentives or discounts.

![Tenure](./png/Tenure_Graph.png)

47.4% of customers churn in their first year, then drop sharply to 9.5% for customers who’ve been around 4+ years. This shows you the first year is the most critical window — if the business can retain customers beyond the 12-month mark, they become significantly more loyal. Onboarding experience and early engagement are the key levers here.

![Internet_Service](./png/Internet%20Service_Graph.png) 

Fiber optic customers churn at ~42%, more than double the rate of DSL customers at 19%. This is concerning, because fiber optic is the top-of-the-line, more expensive service. This may indicate service quality issues, unmet expectations or tough competition in this segment. For those who do not have internet service, the churn rate is only 7.4%. This tells us that the dissatisfaction is really with the internet product.

![Charges](./png/Charges_Graph.png)

Customers who churned were paying an average of ~$74/month than ~$61 for those who stayed. That’s a $13 difference, meaning that churned customers are on more expensive plans — probably fiber optic or premium services — but don’t feel they’re getting enough value for the money. “The business has to figure out if the high-paying customers are getting what they’re paying for.”

![Risk_Segment](./png/Risk%20Segment.png)

The Random Forest model predicted that 1,500+ customers are high risk i.e. they have more than 66% probability of churning. The distribution is highly polarised with only ~500 medium risk customers. Customers are either very likely to leave or very likely to stay, with little in between. This gives the business a clear and actionable target. Instead of spreading retention efforts across the board, they can focus their resources directly on the high risk segment to maximize impact.

## Executive Summary

The analysis uses descriptive and predictive techniques to give a complete picture of customer churn for a telecom company. Python and Pandas were used to clean, transform and enrich the raw customer data with engineered features like tenure groups, charge tiers and service counts. Then we used SQL queries to surface the key patterns in the data. Finally we trained a Random Forest classification model to assign a churn probability score to each customer.

The descriptive analysis told a very clear story. Customers are churning at more than 40% month to month, or more than 14 times the rate of two-year customers, which shows that flexibility comes at a cost to the business. In fact, nearly half of all customers churn in the first year, falling dramatically to 9.5% for those who make it past four years. That means that the first 12 months are the single most important window for retention. Fiber optic subscribers are the premium level, but they churn at 42%, more than twice the rate of DSL customers, indicating a disconnect between price and perceived value. Lost customers also pay on average $13 more per month than retained customers which indicates the business is losing its highest paying customers the fastest.

The predictive model was a supervised learning model. Customer attributes such as contract type, tenure, internet service, payment method and number of services were encoded and fed into a Random Forest classifier trained on 80% of the data and validated on the remaining 20%. The model achieved a ROC-AUC of 0.82, which indicates that the model correctly distinguishes churners from non-churners 82% of the time. Each customer was then assigned a churn probability and placed into one of three segments—Low Risk, Medium Risk, or High Risk. Currently, there are over 1,500 customers in the high risk segment with >66% probability of churning. The distribution is highly polarized with very few medium risk customers. This means customers are either strongly committed or strongly at risk. The business is not facing any pricing issues. It has a value and retention problem that is targeted at a specific and identifiable customer profile: new customers, on flexible contracts, using fiber optic service. The predictive model provides the business with something actionable that a historical analysis cannot: a prioritized list of customers to intervene with before they churn. The clearest path to reducing churn is focused retention efforts on the high risk segment, stronger onboarding in the first year and incentives to move month-to-month customers onto longer contracts.

## Tools Used

Python: Imported raw data from Kaggle, which had a total of 7043 telco customers. Used Pandas for data cleaning and transformation which involved fixing blank TotalCharges values, converting SeniorCitizen to readable labels and creating new features like Tenure Group, Charge Tier and Number of Services. We used scikit-learn to build a Random Forest classification model to predict the probability of churn for each customer and achieved a ROC-AUC score of 0.82.

Pandas: Data Cleaning, Transformation & Feature Engineering. Standardized column names, dealt with missing values, created customer segmentation fields, and exported the final cleaned data set for SQL and Tableau.

scikit-learn: Random Forest classifier trained on 80% of the data and validated on 20% of the data. LabelEncoder was used for encoding categorical features, classification report and ROC-AUC score were used to evaluate model performance, churn probability score and risk segment label were generated for each customer.

SQL (SQLite through DBeaver): Imported cleaned data set into a relational database and wrote analytical queries to find churn rate by contract type, tenure group, internet service, average monthly charges for churned vs retained customers, and customer distribution by risk segment.

Tableau Public: Developed a standalone customer churn analysis dashboard by combining five interactive visualizations that examined key churn drivers by contract type, tenure, internet service, monthly charges, and predicted risk segment.

GitHub: Public hosting and version control of the project's repository including the python pipeline script, SQL query files, cleaned output data, and README documentation for portfolio presentation.

## Dashboard

[Telco Customer Churn Analysis](https://public.tableau.com/app/profile/raianul.quader/viz/TelcoCustomerChurnAnalysis_17777878179300/Dashboard1)

## Data Source

Data sourced from the [Telco Customer Churn dataset on Kaggle](https://www.kaggle.com/code/emineyetm/telco-customer-churn/notebook), uploaded by Emine Bozkus, PhD, originally provided by IBM. The dataset contains 7,043 customer records with demographic, account, and service information used to analyze and predict customer churn.
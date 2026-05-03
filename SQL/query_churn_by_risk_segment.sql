SELECT 
    Risk_Segment,
    COUNT(*) AS Total_Customers,
    SUM(Churn_Binary) AS Churned,
    ROUND(AVG(Churn_Probability_Pct), 1) AS Avg_Churn_Probability
FROM customers
GROUP BY Risk_Segment
ORDER BY Avg_Churn_Probability DESC;
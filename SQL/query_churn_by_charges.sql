SELECT 
	Churn,
	ROUND(AVG(Monthly_Charges), 2) AS Avg_Monthhly_Charges,
	ROUND(AVG(Total_Charges), 2) AS Avg_Total_Charges
FROM customers
GROUP BY Churn;
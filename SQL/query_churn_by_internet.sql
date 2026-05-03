SELECT
	Internet_Service,
	COUNT(*) AS Total_Customers,
	SUM(Churn_Binary) AS Churned,
	ROUND(AVG(Churn_Binary) * 100, 1) AS Churn_Rate_Pct
FROM customers
GROUP BY Internet_Service
ORDER BY Churn_Rate_Pct DESC;
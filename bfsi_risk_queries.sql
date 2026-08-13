-- ====================================================================
-- PROJECT: BFSI Customer Attrition & Risk Analytics
-- TOOL: SQL / DuckDB
-- TARGET TABLE: bank_customers
-- ====================================================================

-- --------------------------------------------------------------------
-- Query A: Regional Risk & Lost Capital Analysis
-- Purpose: Aggregates total customers, churned count, churn rate %,
--          average credit score, and lost capital per country.
-- --------------------------------------------------------------------
SELECT 
    Geography,
    COUNT(CustomerId) AS Total_Customers,
    SUM(Churn) AS Churned_Customers,
    ROUND(SUM(Churn) * 100.0 / COUNT(CustomerId), 2) AS Churn_Rate_Pct,
    ROUND(AVG(CreditScore), 0) AS Avg_Credit_Score,
    ROUND(SUM(CASE WHEN Churn = 1 THEN Balance ELSE 0 END), 2) AS Total_Lost_Capital_USD
FROM bank_customers
GROUP BY Geography
ORDER BY Churn_Rate_Pct DESC;


-- --------------------------------------------------------------------
-- Query B: Top Churned VIPs per Country (SQL Window Function)
-- Purpose: Uses CTE and DENSE_RANK() to identify the top 3 highest-balance
--          churned customers per country for targeted retention outreach.
-- --------------------------------------------------------------------
WITH RankedCustomers AS (
    SELECT 
        Geography,
        CustomerId,
        Surname,
        Balance,
        CreditScore,
        DENSE_RANK() OVER (PARTITION BY Geography ORDER BY Balance DESC) AS Rank_In_Country
    FROM bank_customers
    WHERE Churn = 1
)
SELECT * 
FROM RankedCustomers 
WHERE Rank_In_Country <= 3;
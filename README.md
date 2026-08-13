# BFSI Customer Churn & Capital Risk Analytics

An end-to-end data analytics and predictive risk modeling project investigating customer churn, regional capital exposure, and high-risk demographic trends across a commercial retail banking dataset of 10,000 customers.

## Key Highlights
- Geographic Risk: While France (16.15%) and Spain (16.67%) show lower attrition, Germany exhibits a 32.44% churn rate, accounting for $97.97M in lost capital.
- Product Friction: Customers holding 3 or 4 banking products hit near-100% churn probability, indicating severe fee structure or onboarding friction for multi-product accounts.
- Demographics & VIP Exposure: Churn heavily concentrates in the 40-55 age demographic. Individual churned balances exceeded $250,000 in Spain and $238,000 in France.

## Analytical Workflow
1. SQL Database Architecture (DuckDB): Ingested 10,000 customer records to compute churn rates, average credit scores, and lost capital per country.
2. Advanced SQL Window Functions: Used CTEs and DENSE_RANK() to extract top high-balance churned VIPs per region for targeted retention outreach.
3. Python Exploratory Analysis: Visualized age distribution against churn using KDE plots and analyzed product holding probability rates using Seaborn and Matplotlib.
4. Interactive Dashboarding: Built executive reports tracking total churned balance, credit scores, and regional slicers.

## Tech Stack & Tools Used
SQL (DuckDB), Python (Jupyter Notebooks, Pandas, Seaborn, Matplotlib), Microsoft Excel, Power BI.

## Strategic Recommendations
- Prioritize Regional Retention in Germany: Allocate priority retention campaigns and dedicated relationship managers to German accounts to curb the 32.44% churn rate.
- Product Bundle Audit: Conduct an immediate operational audit on multi-product accounts (3+ products) to eliminate fee friction and improve onboarding retention.
- Wealth Preservation Programs: Introduce tailored wealth management and financial planning offers for high-balance clients aged 40-55.


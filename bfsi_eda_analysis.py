# ====================================================================
# PROJECT: BFSI Customer Attrition & Risk Analytics
# TOOL: Python (Pandas, DuckDB, Seaborn, Matplotlib)
# ====================================================================

import duckdb
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------------------------
# 1. Data Ingestion & SQL Database Initialization
# --------------------------------------------------------------------
url = "https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Bank%20Churn%20Modelling.csv"
duckdb.sql(f"CREATE OR REPLACE TABLE bank_customers AS SELECT * FROM read_csv_auto('{url}', header=True)")

# Load into Pandas DataFrame for visualization
df = duckdb.sql("SELECT * FROM bank_customers").df()

# Set global visual aesthetic
sns.set_theme(style="whitegrid")

# --------------------------------------------------------------------
# 2. Visual 1: Churn Distribution by Customer Age
# Insights: Highlights churn concentration in the 40–55 age demographic.
# --------------------------------------------------------------------
plt.figure(figsize=(10, 5))
sns.histplot(data=df, x="Age", hue="Churn", kde=True, bins=30, palette={0: "#2ecc71", 1: "#e74c3c"})
plt.title("BFSI Risk Analysis: Customer Churn Concentration by Age", fontsize=14, fontweight="bold")
plt.xlabel("Customer Age")
plt.ylabel("Customer Count")
plt.show()

# --------------------------------------------------------------------
# 3. Visual 2: Impact of Product Holdings on Churn Probability
# Insights: Uncovers near-100% churn risk for customers with 3+ products.
# --------------------------------------------------------------------
plt.figure(figsize=(8, 4))
sns.barplot(data=df, x="Num Of Products", y="Churn", errorbar=None, palette="Blues_d")
plt.title("Impact of Product Holdings on Churn Probability", fontsize=14, fontweight="bold")
plt.ylabel("Churn Rate (0.0 to 1.0)")
plt.xlabel("Number of Banking Products Owned")
plt.show()
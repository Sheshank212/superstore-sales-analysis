import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output folder if it doesn't exist
output_dir = "eda_outputs"
os.makedirs(output_dir, exist_ok=True)

# Load cleaned data
df = pd.read_csv("cleaned_superstore.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'])

# --- 1. Total Sales by Category ---
plt.figure(figsize=(8, 5))
sns.barplot(x='Category', y='Sales', data=df, estimator=sum)
plt.title("Total Sales by Category")
plt.tight_layout()
plt.savefig(f"{output_dir}/sales_by_category.png")
plt.show()
plt.close()

# --- 2. Profit by Region ---
plt.figure(figsize=(10, 5))
sns.barplot(x='Region', y='Profit', data=df, estimator=sum)
plt.title("Total Profit by Region")
plt.tight_layout()
plt.savefig(f"{output_dir}/profit_by_region.png")
plt.show()
plt.close()

# --- 3. Top 10 Products by Sales ---
top_products = df.groupby("Product Name")["Sales"].sum().nlargest(10)
plt.figure(figsize=(10, 6))
top_products.plot(kind="barh")
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.tight_layout()
plt.savefig(f"{output_dir}/top_products_by_sales.png")
plt.show()
plt.close()

# --- 4. Monthly Sales Trend ---
df['Order Month'] = df['Order Date'].dt.to_period("M")
monthly_sales = df.groupby("Order Month")["Sales"].sum()
monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(12, 6))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{output_dir}/monthly_sales_trend.png")
plt.show()
plt.close()

print("All EDA plots saved in 'eda_outputs/' folder.")

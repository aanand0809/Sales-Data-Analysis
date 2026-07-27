import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("data/sales_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# -------------------------------
# Graph 1: Monthly Sales Trend
# -------------------------------
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------
# Graph 2: Top 10 Products
# -------------------------------
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------------
# Graph 3: Sales by Category
# -------------------------------
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(6,6))
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales by Category")
plt.ylabel("")
plt.tight_layout()
plt.show()

# -------------------------------
# Graph 4: Profit by City
# -------------------------------
city_profit = df.groupby("City")["Profit"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
city_profit.plot(kind="bar")
plt.title("Profit by City")
plt.xlabel("City")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------------
# Summary
# -------------------------------
print("\n===== DATA SUMMARY =====")
print(df.describe())

print("\nTotal Sales :", df["Sales"].sum())
print("Total Profit :", df["Profit"].sum())

print("\nTop 5 Products:")
print(top_products)

print("\nSales by Category:")
print(category_sales)

print("\nProfit by City:")
print(city_profit)
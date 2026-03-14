import pandas as pd
import matplotlib.pyplot as plt


plt.figure()

# Load dataset
df = pd.read_csv("superstore_sales.csv", encoding="latin1")

# Show first rows
print("First 5 rows:")
print(df.head())

# Total Sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Category:")
print(category_sales)

# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:")
print(region_sales)

# Plot Category Sales
plt.figure()
category_sales.plot(kind="bar", title="Sales by Category")
plt.ylabel("Sales")
plt.savefig("sales_by_category.png")
plt.show()

# Plot Region Sales
plt.figure()
region_sales.plot(kind="bar", title="Sales by Region")
plt.ylabel("Sales")
plt.savefig("sales_by_region.png")
plt.show()
import pandas as pd

# Load the uploaded dataset
# file_path = "/Car_sales.csv"
car_sales = pd.read_csv("Car_sales.csv")

# Show the first few rows to understand the structure
car_sales.head()

import matplotlib.pyplot as plt
import plotly.express as px

# Clean data: drop rows with missing sales values
car_sales_clean = car_sales.dropna(subset=['Sales_in_thousands'])

# Aggregate sales by Model (in case of duplicates)
sales_by_model = car_sales_clean.groupby('Model')['Sales_in_thousands'].sum().sort_values(ascending=False)

# ---------------- MATPLOTLIB VISUALS ----------------

# Bar Chart (Top 10 Models)
plt.figure(figsize=(12,6))
sales_by_model.head(10).plot(kind='bar', color='skyblue')
plt.title("Top 10 Car Models by Sales", fontsize=16)
plt.xlabel("Car Model", fontsize=12)
plt.ylabel("Sales (in thousands)", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Pie Chart (Top 10 Models)
plt.figure(figsize=(8,8))
sales_by_model.head(10).plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='tab20')
plt.title("Sales Distribution Among Top 10 Car Models", fontsize=16)
plt.ylabel("")  # Remove y-label for neatness
plt.show()

# ---------------- PLOTLY INTERACTIVE VISUALS ----------------

# Interactive Bar Chart
fig_bar = px.bar(
    sales_by_model.head(10).reset_index(),
    x="Model", y="Sales_in_thousands",
    title="Top 10 Car Models by Sales (Interactive)",
    labels={"Sales_in_thousands":"Sales (in thousands)", "Model":"Car Model"},
    color="Sales_in_thousands", 
    color_continuous_scale="Blues"
)
fig_bar.show()

# Interactive Pie Chart
fig_pie = px.pie(
    sales_by_model.head(10).reset_index(),
    names="Model", values="Sales_in_thousands",
    title="Sales Distribution Among Top 10 Car Models (Interactive)",
    hole=0.3
)
fig_pie.show()
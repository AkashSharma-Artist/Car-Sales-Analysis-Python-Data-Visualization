import pandas as pd 

#upper import kiye panda taki vo data ko padhe  or manipulate kre yani ki apne husab se smjhee ek series or frame me takdil kre
#mostly mann krr chlo ki data analysis  ke liye

# file_path = "/Car_sales.csv"
car_sales = pd.read_csv("Car_sales.csv") #file jiske read krega panda bhai or dataframe bana krr car_sales 
#nam se assign krdiya yani pura table sab me

# Show the first few rows to understand the structure
car_sales.head() #starting ke 5 show krr rha

import matplotlib.pyplot as plt
import plotly.express as px

# matplotlib.pyplot (plt) is used for static plots (PNG / PDF) — great for reports.

# plotly.express (px) creates interactive plots that you can hover, zoom, and embed into HTML dashboards.

# Clean data: drop rows with missing sales values
car_sales_clean = car_sales.dropna(subset=['Sales_in_thousands'])
# dropna(subset=[...]) removes rows where Sales_in_thousands is NaN (missing). 
# We must remove these because sales values are needed for plotting/aggregation.
# Result is assigned to car_sales_clean, leaving original car_sales unchanged.

# Aggregate sales by Model (in case of duplicates)
sales_by_model = car_sales_clean.groupby('Model')['Sales_in_thousands'].sum().sort_values(ascending=False)

# groupby('Model') groups rows by the Model column. Useful if the same model appears multiple times in the file.
# ['Sales_in_thousands'].sum() sums the sales for each model — i.e., total sales per model.
# .sort_values(ascending=False) sorts that Series in descending order (highest-selling model first).
# sales_by_model is a pandas Series indexed by Model, values are total sales (still in thousands).
# Gotcha: If Sales_in_thousands is a string column, you may need to convert it to numeric first (pd.to_numeric) — 
# but read_csv often infers numeric types automatically.

# ---------------- MATPLOTLIB VISUALS ----------------

# Bar Chart (Top 10 Models)
plt.figure(figsize=(12,6))  #fig ka size
sales_by_model.head(10).plot(kind='bar', color='skyblue') #top 10 sales valo ka bar graph me in skyblue color
plt.title("Top 10 Car Models by Sales", fontsize=16) #title diya hai yeh
plt.xlabel("Car Model", fontsize=12) #x lable
plt.ylabel("Sales (in thousands)", fontsize=12) #y sles bta rha NOTE ye hthousand yani K bolra 20000 ke badle 20 likha hai
plt.xticks(rotation=45, ha='right') #jo niche ke 10 ke lable ho vo tedha show ho taki size ke krnn baju pe na cahdh jayee
plt.tight_layout() #Adjusts padding so labels/title fit inside the figure (avoids cut-off labels).
plt.show()

# Pie Chart (Top 10 Models)
plt.figure(figsize=(8,8))
sales_by_model.head(10).plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='tab20')
plt.title("Sales Distribution Among Top 10 Car Models", fontsize=16)
plt.ylabel("")  # Remove y-label for neatness
plt.show()

# Again we use the top 10 models.

# kind='pie' tells pandas to draw a pie chart from the Series.

# autopct='%1.1f%%' shows percentage labels on slices with 1 decimal place (e.g., 21.2%). out of all me jitna hai usse percent nikl gya

# startangle=140 rotates the start angle so slices are positioned nicely.

# colormap='tab20' uses matplotlib’s tab20 color palette (gives up to 20 distinct colors).

# ---------------- PLOTLY INTERACTIVE VISUALS ----------------

# Interactive Bar Chart
fig_bar = px.bar(
    sales_by_model.head(10).reset_index(),
    x="Model", y="Sales_in_thousands",
    title="Top 10 Car Models by Sales (Interactive)",
    labels={"Sales_in_thousands":"Sales (in thousands)", "Model":"Car Model"}, #iska koi roll nhi hover me vo buss 
    #lable change hua hai ki isted of 1st yeh show kre
    color="Sales_in_thousands", 
    color_continuous_scale="Blues"
)

# sales_by_model.head(10).reset_index():

# sales_by_model.head(10) selects top 10 (Series).

# .reset_index() converts the Series into a DataFrame with columns Model and Sales_in_thousands (needed because Plotly expects a DataFrame).

# px.bar(...) builds an interactive bar chart:

# x="Model" and y="Sales_in_thousands" map DataFrame columns to axes.

# title= sets the chart title.

# labels={...} changes axis labels that appear in hover tooltips and axis titles.

# color="Sales_in_thousands" colors bars according to their value (adds a color scale).

# color_continuous_scale="Blues" chooses a blue gradient for the color scale.

# The px chart is interactive: hover shows exact values, you can zoom, pan, and toggle visibility.


fig_bar.show()

# Interactive Pie Chart
fig_pie = px.pie(
    sales_by_model.head(10).reset_index(),
    names="Model", values="Sales_in_thousands",
    title="Sales Distribution Among Top 10 Car Models (Interactive)",
    hole=0.3
)
fig_pie.show()


# px.pie creates an interactive pie chart.

# names="Model" defines slice labels.

# values="Sales_in_thousands" defines numeric slice sizes.

# hole=0.3 creates a donut chart with a 30% hole in the center (often easier to read).

# Hovering a slice shows the model, value, and percentage.
# Car Sales Analysis – Python Data Visualization

This project analyzes a car sales dataset to identify top-performing car 
models by sales volume, using Python for data cleaning, aggregation, and 
visualization. It demonstrates both static (Matplotlib) and interactive 
(Plotly) charting approaches on the same dataset for comparison.

## Dataset
`Car_sales.csv` — contains manufacturer, model, sales figures, pricing, 
and technical specifications (engine size, horsepower, fuel efficiency, etc.) 
for various car models.

## Workflow
1. **Data Loading** — Read CSV into a Pandas DataFrame
2. **Data Cleaning** — Removed rows with missing `Sales_in_thousands` values
3. **Aggregation** — Grouped and summed sales by car `Model`, sorted to find top performers
4. **Static Visualization (Matplotlib)**
   - Bar chart: Top 10 car models by sales
   - Pie chart: Sales distribution among top 10 models
5. **Interactive Visualization (Plotly)**
   - Interactive bar chart with hover tooltips and color scale
   - Interactive donut chart for sales distribution

## Features
- Data cleaning & aggregation with Pandas (`groupby`, `dropna`, `sort_values`)
- Side-by-side comparison of static vs. interactive visualization libraries
- Interactive charts with hover, zoom, and color-scaled bars
- Donut-style pie chart for cleaner distribution reading

## Tech Stack
- Python
- Pandas (data cleaning & aggregation)
- Matplotlib (static visualizations)
- Plotly Express (interactive visualizations)

## Key Insights
- Identified the top 10 best-selling car models by total sales volume
- Compared traditional reporting-style charts (Matplotlib) with interactive, 
  dashboard-ready charts (Plotly) on the same data

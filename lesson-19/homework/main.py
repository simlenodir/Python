# Bismillah
import pandas as pd
import numpy as np

sales_data = pd.read_csv('sales_data.csv')
sales_data

# Task 1 
Total = sales_data.groupby('Category').sum('Quantity')
Total1 = sales_data.groupby('Category')['Quantity'].agg('sum')
Total2 = sales_data.groupby('Category')['Quantity'].sum()
print(Total)

# Task 1-2 
# Sum of total price and quantity per category
sales_price = sales_data.groupby('Category')['Price'].sum()
sales_unit = sales_data.groupby('Category')['Quantity'].sum()

# Average price per unit
avg_price_unit = sales_price / sales_unit

avg_price_unit = avg_price_unit.reset_index(name='Avg_Price_Per_Unit')
print(avg_price_unit)

# Task 1-3 
max_quantity = sales_data.groupby(['Category', 'Date'])['Quantity'].max().reset_index()
print(max_quantity)

 # 1-2

product_sales = sales_data.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()

# Sort within each category to get the top-selling product
top_category_products = product_sales.sort_values(['Category', 'Quantity'], ascending=False)

# Drop duplicates to keep only the top product per category
top_selling = top_category_products.drop_duplicates('Category')
print(top_selling)

# Task 1-3 Find the date on which the highest total sales (quantity * price) occurred.
sales_data['Max_Sales'] = sales_data['Price'] * sales_data['Quantity']
total_sales_date = sales_data.groupby('Date')['Max_Sales'].sum().reset_index()
# total_sales_date.sort_values('Max_Sales', ascending=False).head(1)

max_date = total_sales_date.loc[total_sales_date['Max_Sales'].idxmax()]
print(max_date)

# Starting 2-Task
customers = pd .read_csv('customer_orders.csv')
# 2-1Filter customers who made at least 20 orders
filtered_customers = customers.groupby('CustomerID').filter(lambda x: len(x) >= 20)

print(filtered_customers)

# 2-2 Identify customers who have ordered products with an average price per unit greater than $120.
customers['PricePerUnit'] = customers['Price'] / customers['Quantity']

avg_per_customer = customers.groupby('CustomerID')['PricePerUnit'].mean().reset_index()

high_value_customer = avg_per_customer[avg_per_customer['PricePerUnit'] > 120]

print(high_value_customer)

# Task 2-3 Group by Product and calculate total quantity and total price
summary = customers.groupby('Product').agg(
    Total_Quantity = ('Quantity', 'sum'),
    Total_Price = ('Price', lambda x: (x * customers.loc[x.index, 'Quantity']).sum())
).reset_index()

summary = summary[summary['Total_Quantity']>= 5]
print(summary)

# Task 3-1 "population.db" sqlite database has population table.

import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect('population.db')

query = "Select * from population"

population_df = pd.read_sql_query(query,conn)

print(population_df.head())
conn.close()

# Task 3-2 "population salary analysis.xlsx" file defines Salary Band categories
salary_band_df = pd.read_excel('population_salary_analysis.xlsx')
print(salary_band_df)

# Assuming salary_band_df defines continuous ranges
salary_band_df.columns = salary_band_df.columns.str.strip()
salary_band_df

# Creating Function Convert string to int
def parse_salary_band(band):
    band = band.replace('$', '').replace(',', '').strip().lower()
    
    if band.startswith('till'):
        max_salary = int(band.replace('till', ''))
        return (0, max_salary)
    elif "and over" in band:
        min_salary = int(band.replace('and over', '').strip())
        return (min_salary, np.inf)
    elif "-" in band:
        parts = band.split('-')
        min_salary = int(parts[0].strip())
        max_salary = int(parts[1].strip())
        return (min_salary, max_salary)
    else:
        return (np.nan, np.nan)
    
    salary_band_df[['Max_Salary', 'Min_Salary']] = salary_band_df['Salary Band'].apply(
    lambda x: pd.Series(parse_salary_band(x))
)

# Create bins and labels
# First, sort by Min_Salary to ensure monotonic bins
salary_band_df = salary_band_df.sort_values(by='Min_Salary')

# Reset index after sorting (optional but cleaner)
salary_band_df = salary_band_df.reset_index(drop=True)

# Now build the bins safely
bins = salary_band_df['Min_Salary'].tolist() + [salary_band_df['Max_Salary'].iloc[-1]]

# Remove any duplicates in the bins
bins = sorted(set(bins))  # ensures monotonic increasing

labels = salary_band_df['Salary Band']

# Now use pd.cut
population_df['SalaryBand'] = pd.cut(population_df['salary'], bins=bins, labels=labels, right=False)


summary = population_df.groupby('SalaryBand').agg(
    PopulationCount=('salary', 'count'),
    AverageSalary=('salary', 'mean'),
    MedianSalary=('salary', 'median')
).reset_index()

summary['Pesentage'] = round((summary['PopulationCount'] / population_df['id'].count()) * 100, 2)
summary['AverageSalary'] = summary['AverageSalary'].fillna(0)
summary['MedianSalary'] = summary['MedianSalary'].fillna(0)
print(summary)

# Task 3-3 Calculate the same measures in each State

summary1 = population_df.groupby('state').agg(
    PopulationCount=('salary', 'count'),
    AverageSalary=('salary', 'mean'),
    MedianSalary=('salary', 'median')
).reset_index()

summary1['Pesentage'] = round((summary1['PopulationCount'] / population_df['id'].count()) * 100, 2)
summary1['AverageSalary'] = summary1['AverageSalary'].fillna(0)
summary1['MedianSalary'] = summary1['MedianSalary'].fillna(0)
print(summary1)

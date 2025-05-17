import pandas as pd
import matplotlib.pyplot as plt

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# Task: 1-1
# Average of all subjects per student (after groupby)
# Exercise 1: Calculate the average grade for each student.
avg_student = df1.groupby('Student_ID')[['Math', 'English', 'Science']].mean()
avg_student['Average_Grade'] = avg_student.mean(axis=1)
avg_student = avg_student[['Average_Grade']]
print(avg_student)

# Task: 1-2
# Exercise 2: Find the student with the highest average grade.
avarage_student = df1.groupby('Student_ID')[['Math', 'English', 'Science']].mean()
avarage_student['Avarage_Grade'] = avarage_student.mean(axis = 1)
highest_avg_student = avarage_student.sort_values('Avarage_Grade', ascending=False).head(1)
print(highest_avg_student)

# Task: 1-3
# Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.

df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
print(df1)

# Task: 1-4
# Exercise 4: Plot a bar chart to visualize the average grades in each subject.

subject_averages = df1[['Math', 'English', 'Science']].mean()

# Plot bar chart
plt.figure(figsize=(8, 5))
subject_averages.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])

plt.title('Average Grades in Each Subject')
plt.ylabel('Average Grade')
plt.xlabel('Subject')
plt.ylim(0, 100)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# Data for 2-task
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
print(df2)

# Task: 2-1
# Exercise 1: Calculate the total sales for each product.
Total_Sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print(Total_Sales)

# Task: 2-2
# Exercise 2: Find the date with the highest total sales.
highest_total = df2.groupby('Date').sum()
highest_total = highest_total.loc[highest_total['Total'].idxmax()]
print(highest_total)

# Task: 2-3
# Exercise 3: Calculate the percentage change in sales for each product from the previous day.
df2['Product_A_Change%'] = df2['Product_A'].pct_change() * 100
df2['Product_B_Change%'] = df2['Product_B'].pct_change() * 100
df2['Product_C_Change%'] = df2['Product_C'].pct_change() * 100 

df2 = df2.round(2)
df2

# Task: 2-4
# Exercise 4: Plot a line chart to visualize the sales trends for each product over time.
# Plot
plt.figure(figsize=(10, 6))

plt.plot(df2['Date'], df2['Product_A'], marker='o', label='Product A', color='blue')
plt.plot(df2['Date'], df2['Product_B'], marker='s', label='Product B', color='green')
plt.plot(df2['Date'], df2['Product_C'], marker='^', label='Product C', color='red')

plt.title('Sales Trends for Products A, B, and C Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=90)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

plt.show()

# Data Frame for task 3
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# Task: 3-1
# Exercise 1: Calculate the average salary for each department.
avarage_salary_depart = df3.groupby('Department')['Salary'].mean()
avarage_salary_depart.round(2)

# Task: 3-1
# Exercise 1: Calculate the average salary for each department.
avarage_salary_depart = df3.groupby('Department')['Salary'].mean()
avarage_salary_depart.round(2)

# Task: 3-2
# Exercise 2: Find the employee with the most experience

most_experience = df3.loc[df3['Experience (Years)'].idxmax()]
most_experience

# Exercise 3-3: Create a new column 'Salary Increase'
# representing the percentage increase in salary from the minimum salary in the dataframe.

# min_salary = df3.loc[df3['Salary'].idxmin()]
min_salary = df3['Salary'].min()
min_salary
# Step 2: Calculate the salary increase percentage
df3['Salary Increase'] = (df3['Salary'] / min_salary * 100).round(2)
df3

# Task: 3-4
# Count employees per department
department_counts = df3['Department'].value_counts()

# Plot
plt.figure(figsize=(8, 5))
department_counts.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Employee Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

import seaborn as sns

plt.figure(figsize=(8, 5))
sns.countplot(x='Department', data=df3, palette='pastel', edgecolor='black')

plt.title('Employee Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

# Task: 4-1
# Exercise 1: Calculate the total revenue from all orders.
df4['Unit_price'] = df4['Total_Price'] / df4['Quantity']
# Calculate total revenue
Total_Revenue = df4['Total_Price'].sum()
print(Total_Revenue)

# Task: 4-2
# Exercise 2: Find the most ordered product

most_ordered_Product = df4['Product'].value_counts().head(1)
# most_ordered_Product.sort_values(ascending= False).head(1)
print(most_ordered_Product)

# Task: 4-3
# Exercise 3: Calculate the average quantity of products ordered.
avg_products_ordered = df4['Quantity'].mean()
avg_products_ordered


# Task: 4-4
# Group total sales by product
sales_by_product = df4.groupby('Product')['Total_Price'].sum()

# Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(sales_by_product, labels=sales_by_product.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)

plt.title('Sales Distribution by Product')
plt.axis('equal')  # Ensures the pie is circular
plt.tight_layout()
plt.show()

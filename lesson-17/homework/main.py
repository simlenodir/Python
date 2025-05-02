# Bismillah
# Alhamdulillah

import pandas as pd
import numpy as np
# Task 1-1

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)

df = df.rename(columns= {'Age': 'age', 'First Name': 'first_name'})


print(df)

# Task 1-2
first_3_rows = df.head(3)
print(first_3_rows)

# Task 1-3
mean_age  = df['age'].mean()
print('Mean age: ', mean_age)

# Select and print only the 'Name' and 'City' columns
# Task 4
df_select = df[['first_name', 'City' ]]
print(df_select)

# Task 1-5
# Add a new column 'Salary' with random salary values

df['Salary'] = np.random.randint(50000, 100001, size =len(df))

print(df)

# Task 1-6
# Display summary statistics of the DataFrame
df_statics = df.describe(include= 'all')
print(df_statics)

# Bismillah
# Task 2-1

data ={
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'], 
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500],
}

df = pd.DataFrame(data)
print(df)

# Task 2-2
# Calculate and display the maximum sales and expenses.

max_sales = df['Sales'].max()
max_expenses = df['Expenses'].max()
print(f'Max sales: {max_sales} \n')
print(f'Max expenses: {max_expenses}')

# Task 2-3
# Calculate and display the minimum sales and expenses.

min_sales = df['Sales'].min()
min_expenses = df['Expenses'].min()

print(f'min sales: {min_sales} \n')
print(f'min expenses: {min_expenses}')

# Task 2-4
# Calculate and display the average sales and expenses.

avg_sales = df['Sales'].mean()
avg_expenses = df['Expenses'].mean()

print(f'Avarage sales: {avg_sales}')
print(f'Avarage expenses: {avg_expenses}')

# Bismillah
# Task 3-1

data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertaiment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

df = pd.DataFrame(data)
df

# Task 3-1
# Calculate and display the maximum expense for each category.

df['Max_expenses'] = df[['January', 'February', 'March', 'April']].max(axis=1)
print(df[['Category', 'Max_expenses']])

# Task 3-2
# Calculate and display the maximum expense for each category.

df['Max_expenses'] = df[['January', 'February', 'March', 'April']].max(axis=1)
print(df[['Category', 'Max_expenses']])

# Task 3-3
# Calculate and display the minimum expense for each category.

df['Min_expenses'] = df[['January', 'February', 'March', 'April']].min(axis= 1)
print(df[['Category', 'Min_expenses']])

# Define the data again to ensure 'Category' is present
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertaiment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

# Create the DataFrame
df = pd.DataFrame(data)
# Set 'Category' as index
df = df.set_index('Category')

# Calculate average expense for each category (row-wise mean)
df['Average_Expense'] = df.mean(axis=1)

# Display the result
print(df[['Average_Expense']])

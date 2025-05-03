# Bismillah
import pandas as pd
import numpy as np
import os


df1 = pd.read_csv('task/stackoverflow_qa.csv')
df1.head()

# Task 2-1
# Find all questions that were created before 2014
df1['creationdate'] = pd.to_datetime(df1['creationdate'])

filt = df1['creationdate'].dt.year < 2014
print(df1[filt])

# Task 2-2
# Find all questions with a score more than 50

filt_score = df1['score'] > 50
print(df1[filt_score])

# Task 2-3
# Find all questions with a score between 50 and 100

filt_score = df1['score'].between(50, 100)
print(df1[filt_score])

# Task 2-4
# Find all questions answered by Scott Boston

filt_name = df1['ans_name'].str.strip()  == 'Scott Boston'
print(df1[filt_name])

users = ['Mike Pennington', 'Scott Boston', 'Demitri', 'Wes McKinney', 'doug']
filter = df1['ans_name'].isin(users)
print(df1[filter])

# Task 2-6
# Find all questions that were created between March, 2014 and October 2014
# that were answered by Unutbu and have score less than 5.
df1['creationdate'] = pd.to_datetime(df1['creationdate'])

start_date = pd.to_datetime('2014-03-01')
end_date = pd.to_datetime('2014-10-01')

filt_date = df1['creationdate'].between(start_date, end_date)
filt_name = df1['ans_name'] == 'Unutbu'
filt_score = df1['score'] < 5

final_filter = filt_date & filt_name & filt_score
print(df1[final_filter])

# Task 2-7
# Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
filter_score = df1['score'].between(5,10)
filter_view = df1['viewcount'] >10000
filter = filter_score | filter_view

print(df1[filter])

# Task 2-8
# Find all questions that are not answered by Scott Boston

filt_name = df1['ans_name'] != 'Scott Boston'
print(df1[filt_name])

titanic = pd.read_csv('task/titanic.csv')
titanic.head()

# Task 3-1

filt_female = titanic['Sex'] == 'female'
filt_class = titanic['Pclass'] == 1
filt_age = titanic['Age'].between(20, 30)

full_filt = filt_female & filt_class & filt_age

titanic[full_filt]

# Task 3-2

filt_fare = titanic['Fare'] > 100
titanic[filt_fare]

# Task 3-3

filt_sibsp = titanic['SibSp'] == 0
filt_survived = titanic['Survived'] == 0
filt_patch = titanic['Parch'] == 0

full_filt = filt_sibsp & filt_patch & filt_survived

titanic[full_filt]

# Task 3-4
filt_embarked = titanic['Embarked'] == 'C'
filt_fare = titanic['Fare'] > 50

full_filt = filt_embarked & filt_fare
titanic[full_filt]

# Task 3-5
filt_sibsp = titanic['SibSp'] > 0
filt_parch = titanic['Parch'] > 0

full_filt = filt_parch & filt_sibsp
titanic[full_filt]

# Task 3-6

filt_age = titanic['Age'] <= 15
filt_survived = titanic['Survived'] == 1

full_filt = filt_survived & filt_age 
titanic[full_filt]

# Task 3-7

filt_cabin = titanic['Cabin'].notna()
filt_fare = titanic['Fare'] > 200

full_filt = filt_cabin & filt_fare
titanic[full_filt]

# Task 3-8
filt_id_odd = titanic['PassengerId'] % 2 == 1

titanic[filt_id_odd]

# task 3-9
count_tickets = titanic['Ticket'].value_counts()
unique_tickets = count_tickets[count_tickets == 1].index

filt_unique_ticket = titanic['Ticket'].isin(unique_tickets)

titanic[filt_unique_ticket]

# Task 3-10
filt_name = titanic['Name'].str.contains('Miss')

titanic[filt_name]

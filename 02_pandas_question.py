# # Question 1: Create a DataFrame with Name and Age
# import pandas as pd
# name = ["A", "B", "C"]
# age = [20, 25, 30]
# df = pd.DataFrame({'Name': name, 'Age': age})
# print(df)

# # Question 2: Print only the Age column
# print(df['Age'])
# print()

# # Question 3: Create a Series of marks
# marks = pd.Series([90, 80, 85])
# print(marks)
# print()

# # Question 4: Find the maximum age
# max_age = df['Age'].max()
# print(max_age)
# print()

# # Question 5: Find the minimum age
# min_age = df['Age'].min()
# print(min_age)
# print()

# # Question 6: Use .describe() on your DataFrame
# print(df.describe())
# print()

# # Question 7: Add a new column Salary
# salary = [20000, 30000, 40000]
# df['Salary'] = salary
# print(df)
# print()

# # Question 8: Select multiple columns: Name and Salary
# print(df[['Name', 'Salary']])
# print()

# # Question 9: Print first 2 rows
# print(df.head(2))

# # Question 10:Print last 2 rows
# print(df.tail(2))

# # Question 11:Show people with Age > 22
# age_greater=df[df["Age"]>22]
# print("age_greater")
# print(age_greater)

# # Question 12:Show people with Salary > 25000
# salary_greater=df[df["Salary"]>25000]
# print("More salary")
# print(salary_greater)

# # Question 13.Show only females (if you add gender column)
# df["Gender"]=["Male","Female","Female"]
# print(df)
# only_female=df[df["Gender"]=="Female"]
# print("Only female")
# print(only_female)

# # Question 14.Find average salary
# average=df["Salary"].mean()
# print(average)

# # Question 15.Find total salary
# total_salary=df["Salary"].sum()
# print(total_salary)

# # Question 16.Sort data by Age
# sort_data=df.sort_values(by="Age")
# print(sort_data)

# Question 17
# import pandas as pd
# df = pd.DataFrame({
#     "Name": ["A", "B", "C"],
#     "Age": [20, None, 30],
#     "Salary": [None, 20000, None],
#     "Sex": ["Male","Female","Female"]
# })
# print(df)

# # Question 18:Display the first 5 rows
# # print(df.head(2))

# # Question 19:Check the data types of all columns
# # print(df.dtypes)

# # Question 20:Get full information about the dataset (rows, columns, null values)
# # print(df.info())

# # Question 21:Identify which column has missing values
# df.isna().any()

# # Question 22:Find Total number of rows and columns in dataset
# total_rows=len(df)
# print("Total rows:",total_rows)
# total_columns=len(df.columns)
# print("Total rows:",total_columns)

# # Question 23:Find Which column has the most missing values
# most_missing_value=df.isna().sum()
# print(most_missing_value)

# Datasets
# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan", "Anjali", "Rohit", "Sneha"],
#     "Age": [23, 28, None, 35, 40, 22, None, 30],
#     "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
#     "Salary": [25000, 30000, 20000, None, 50000, 28000, 32000, None],
#     "Department": ["IT", "HR", "IT", "Finance", "IT", "HR", "Finance", "IT"]
# })

# Basics Question
'''1.Show first 5 rows
2.Check data types
3.Get full info of dataset'''

# Question1
# first_5_rows=df.head(5)
# print(first_5_rows)

# Question2
# data_type=df.dtypes
# print("Data Types")
# print(data_type)

# Question3
# information=df.info()
# print("Information")
# print(information)

# Selection Question
'''1.Select only Name and Salary
2.Select only Age column'''
# Question1
# name_salary=df[["Name","Salary"]]
# print(name_salary)

# Question2
# only_age=df[["Age"]]
# print(only_age)

# Filtering Question
'''1.Show people with Age > 25
2.Show people from IT department
3.Show people with Salary > 30000
4.All above 3 condition meet'''
# Question1
# age_greaterthan_25=df[df["Age"]>25]
# print(age_greaterthan_25)

# Question2
# it_department=df[df["Department"]=="IT"]
# print(it_department)

# Question3
# salary_greaterthan_30000=df[df["Salary"]>30000]
# print(salary_greaterthan_30000)

# Question4
# all_condition=df[(df["Age"]>25) & (df["Department"]=="IT") & (df["Salary"]>30000)]
# print(all_condition)

# Missing Question
'''1.Show rows where Age is missing
2.Show rows where Salary is NOT missing'''
# Question1
# age_rows_missing=df[df.isnull().any(axis=1)]
# print(age_rows_missing)

# Question2
# salary_rows_notmissing=df[df['Salary'].notna()]
# print(salary_rows_notmissing)

# Advance Question
'''1.Get names of people with Age > 30
2.Get Name + Salary where Salary > 25000'''
# Question1
# name_age_greaterthan_30=df.loc[df["Age"]>30, ["Name"]]
# print(name_age_greaterthan_30)

# Question2
# name_salary_greaterthan_25000=df.loc[df["Salary"]>25000, ["Name", "Salary"]]
# print(name_salary_greaterthan_25000)


# Dataset 2
import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan", "Anjali", "Rohit", "Sneha"],
    "Age": [23, 28, None, 35, 40, 22, None, 30],
    "Salary": [25000, 30000, 20000, None, 50000, 28000, 32000, None],
    "Bonus": [2000, 3000, 1500, 4000, 5000, 2500, 3500, 3000],
    "Department": ["IT", "HR", "IT", "Finance", "IT", "HR", "Finance", "IT"]
})

# Basic Column Creation
'''Q1. Create a new column:"Double_Age" = Age x 2
Q2. Create a new column:"Salary_in_K" = Salary / 1000
Q3. Create a new column:"Total_Earning" = Salary + Bonus'''

# Question 1
# df["Double_age"]=df["Age"]*2
# print(df)

# Question 2
# df["Salary_in_K"]=df["Salary"]/1000
# print(df)

# Question 3
# df["Total_earning"]=df["Salary"]+df["Bonus"]
# print(df)

# Logical / Real Thinking
'''Q4.Create a new column:"Age_Group"
Condition:
Age < 25 → "Young"
Age ≥ 25 → "Adult"
(Hint: use apply() or conditional logic)

Q5.Create a new column:"High_Earner"
Condition:
Salary > 30000 → "Yes"
Else → "No"'''

# Question 4
import numpy as np
# df["Age_Group"] = df["Age"].apply(lambda x: "Young" if x < 25 else "Adult")
# df["Age_Group"] = np.where(df["Age"] < 25, "Young", "Adult")
# print(df)

# Question 5
# import numpy as np
# df["High_Earner"]=np.where(df["Salary"]>30000,"Yes", "No")
# print(df)

# Column vs Column Operations 
'''Q6.Create a new column:"Bonus_Ratio" = Bonus / Salary
Q7.Create a new column:"Salary_Per_Age" = Salary / Age'''

# Question 6
df["Bonus_Ratio"]=df["Bonus"]/df["Salary"]
print(df)

# Question 7
df["Salary_Per_Age"]=df["Salary"]/df["Age"]
print(df)
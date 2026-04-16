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
# df["Bonus_Ratio"]=df["Bonus"]/df["Salary"]
# print(df)

# Question 7
# df["Salary_Per_Age"]=df["Salary"]/df["Age"]
# print(df)

# Rename Question
'''Q8.Rename:
"Name" → "Employee_Name"
"Salary" → "Monthly_Salary"
Q9.Convert all column names to lowercase'''
# Question 8
# rename_name_salary=df.rename(
#     columns={
#         "Name":"Employee_Name",
#         "Salary":"Monthly_Salary"
#     }
# )
# print(rename_name_salary)

# Question 9
# lower_case=df.rename(columns=str.lower)
# print(lower_case)

# Real-world Thinking
'''Q10.Create a new column:"Tax"
Condition:
Salary > 30000 → Tax = 10% of Salary
Else → Tax = 5% of Salary'''
# import numpy as np
# df["Tax"]=np.where(df["Salary"]>30000, df["Salary"]*0.10,df["Salary"]*0.05)
# print(df)

# New Dataset
'''import pandas as pd

df = pd.DataFrame({
    "Employee_ID": range(1, 16),
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan", "Anjali", "Rohit", "Sneha",
             "Vikas", "Pooja", "Arjun", "Kriti", "Manish", "Riya", "Sahil"],
    "Age": [23, 28, 35, 40, 29, 31, 45, 26, 38, 27, 50, 33, 41, 30, 36],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female",
               "Male", "Female", "Male", "Female", "Male", "Female", "Male"],
    "Department": ["IT", "HR", "Finance", "IT", "IT", "HR", "Finance", "IT",
                   "Finance", "HR", "IT", "Finance", "IT", "HR", "Finance"],
    "Salary": [25000, 30000, 45000, 50000, 28000, 32000, 60000, 27000,
               52000, 29000, 70000, 48000, 55000, 31000, 53000],
    "Experience": [1, 3, 7, 10, 4, 5, 12, 2, 9, 3, 15, 6, 11, 4, 8],
    "Rating": [3.5, 4.0, 4.5, 4.8, 3.9, 4.2, 4.7, 3.8, 4.6, 4.1, 4.9, 4.3, 4.8, 4.0, 4.5]
})'''
# Warm-up Question
'''Q1.Find:Average salary of all employees
Q2.Find:Median experience
Q3.Get full statistical summary of:Salary, Age, Experience'''
# Question 1
# average=df["Salary"].mean()
# print(average)

# Question 2
# med=df["Salary"].median()
# print(med)

# GroupBy Core 
'''Q4.Find:Average salary per department
Q5.Find:Average rating per gender
Q6.Find:Maximum salary in each department'''
# Question 4
# average_salary_dept=df.groupby("Department")["Salary"].mean()
# print(average_salary_dept)

# Question 5
# average_rate_gender=df.groupby("Gender")["Rating"].mean()
# print(average_rate_gender)

# Question 6
# max_by_dept=df.groupby("Department")["Salary"].max()
# print(max_by_dept)

# Multi-Level Grouping (ADVANCED)
'''Q7.Find:Average salary based on:Department,Gender

Q8.Find:Average experience based on:Gender,Department'''

# Question 7
# average_dep_gen=df.groupby(["Department","Gender"])["Salary"].mean()
# print(average_dep_gen)

# Question 8
# average_gen_dep=df.groupby(["Gender","Department"])["Experience"].mean()
# print((average_gen_dep))
# Deep Analytical Thinking
'''Q9.Which department has:Highest average salary
Q10.Which gender has:Higher average rating
Q11.Find:Number of employees in each department
Q12.Find:Count of employees by Gender + Department'''

# Question 9
# highest_avg_sal_dept=df.groupby(["Department"])["Salary"].mean().idxmax()
# print(highest_avg_sal_dept)

# Question 10
# highest_avg_rating=df.groupby(["Gender"])["Rating"].mean().idxmax()
# print(highest_avg_rating)

# # Question 11
# no_of_employee=df.groupby(["Department"])["Name"].count()
# print(no_of_employee)

# Question 12
# count_gen_dept=df.groupby(["Gender","Department"])["Name"].count()
# print(count_gen_dept)

# Advanced Aggregation (PRO LEVEL)
'''Q13.Use .agg() to find:For Salary:
min
max
mean

For Experience:
min
max
Q14.For each department, calculate:
mean salary
max experience
average rating'''

# Question 13
# aggregation_salary=df["Salary"].agg(["min","max","mean"])
# print(aggregation_salary)

# aggregation_exp=df["Experience"].agg(["min","max"])
# print(aggregation_exp)
# Question 14
# aggregation_department = df.groupby(["Department"]).agg({
#     "Salary": "mean",
#     "Experience": "max",
#     "Rating": "mean"
# })
# print(aggregation_department)

# Real Analyst Thinking
'''Q15.Find:Top 3 highest paid employees
Q16.Find:Employees with salary above overall average
Q17.Find:Department where average experience is highest
Q18.Find:Correlation insight (manually think):
Does higher experience → higher salary?
(Hint: compare grouped stats)'''

# Question 15
# top_paid_emp = df.sort_values(by="Salary", ascending=False).head(3)[["Name", "Salary"]]
# print(top_paid_emp)

# Question 16
# average_salary = df["Salary"].mean()
# above_avg_employees = df[df["Salary"] > average_salary]
# print("Employees with salary above overall average:")
# print(above_avg_employees)

# Question 17
# avg_exp_by_dept = df.groupby("Department")["Experience"].mean()
# highest_exp_dept = avg_exp_by_dept.idxmax()
# print(f"Department with highest average experience: {highest_exp_dept}")

# Question 18
# correlation = df["Experience"].corr(df["Salary"])
# print(f"Correlation between Experience and Salary: {correlation}")

import pandas as pd

df = pd.DataFrame({
    "Date": ["2024-01-01","2024-01-01","2024-01-01","2024-01-02","2024-01-02","2024-01-02",
             "2024-01-03","2024-01-03","2024-01-03"],
    "City": ["Delhi","Mumbai","Bangalore","Delhi","Mumbai","Bangalore",
             "Delhi","Mumbai","Bangalore"],
    "Product": ["Laptop","Laptop","Laptop","Phone","Phone","Phone",
                "Tablet","Tablet","Tablet"],
    "Sales": [50000,60000,55000,30000,35000,32000,20000,25000,23000],
    "Units": [5,6,5,10,12,11,8,9,7]
})

# Sorting 
'''Q1.Sort the dataset by:Sales (ascending)
Q2.Sort the dataset by:City and Sales (descending)
Q3.Find:Top 5 highest sales records'''

# Question 1
# sort_sales=df.sort_values(by="Sales",ascending=True)
# print(sort_sales)

# Question 2
# sort_city_sales=df.sort_values(["City","Sales"],ascending=False)
# print(sort_city_sales)

# Question 3
# top_sales=df.sort_values(by="Sales",ascending=False).head(5)
# print(top_sales)

# Understanding Structure
'''Q4.Check:How many unique cities exist
Q5.Check:How many unique products exist'''

# Question 4
# unique_city=df["City"].unique()
# print(unique_city)

# Question 5
# unique_product=df["Product"].unique()
# print(unique_product)

# Pivot 
'''Q6.Create a pivot table:
Index = Date
Columns = City
Values = Sales
Q7.Create a pivot:
Index = Date
Columns = Product
Values = Units'''

# Question 6
# table=df.pivot_table(
#     index="Date",
#     columns="City",
#     values="Sales"
# )
# print(table)

# Question 7
# table1=df.pivot(
#     index="Date",
#     columns="City",
#     values="Units"
# )
# print(table1)

# Pivot Table (Aggregation)
'''Q8.Create pivot_table:
Index = City
Columns = Product
Values = Sales
aggfunc = mean
Q9.Create pivot_table:
Index = Product
Values = Sales
aggfunc = sum
Q10.Create pivot_table:
Index = City
Columns = Product
Values = Units
aggfunc = sum
Include totals (margins=True)'''

# Question 8
# table1=df.pivot_table(
#     index="City",
#     columns="Product",
#     values="Sales",
#     aggfunc="mean"
# )
# print(table1)

# Question 9
# table2=df.pivot_table(
#     index="Product",
#     values="Sales",
#     aggfunc="sum"
# )
# print(table2)

# Question 10
# table3=df.pivot_table(
#     index="City",
#     columns="Product",
#     values="Units",
#     aggfunc="sum",
#     margins=True
# )
# print(table3)

# Melt (Wide → Long)
'''Q11.First create pivot:
Date vs City (Sales)
Then:Convert it back to long format using melt()
Q12.Use melt with:
Custom column names:
var_name = "City_Name"
value_name = "Total_Sales"'''

# Question 11
# table=df.pivot(
#     index="Date",
#     columns="City",
#     values="City"
    
# )
# convert_melt=table.melt()
# print(convert_melt)
# Question 12
# table1=df.melt(
#     var_name="City_Name",
#     value_name="Total_Sales"
# )
# print(table1)

# Real Analyst Thinking
'''Q13.Which city has:Highest total sales
Q14.Which product has:Maximum total units sold
Q15.On which date:Sales were highest overall'''

# Question 13
highest_sales=df.groupby(["City"])["Sales"].mean().idxmax()
print(highest_sales)

# Question 14
highest_product=df.groupby(["Product"])["Units"].mean().idxmax()
print(highest_product)

# Question 15
sale_date_high=df.groupby(["Date"])["Sales"].mean().idxmax()
print(sale_date_high)
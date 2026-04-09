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
import pandas as pd
df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Age": [20, None, 30],
    "Salary": [None, 20000, None],
    "Sex": ["Male","Female","Female"]
})
print(df)

# Question 18:Display the first 5 rows
# print(df.head(2))

# Question 19:Check the data types of all columns
# print(df.dtypes)

# Question 20:Get full information about the dataset (rows, columns, null values)
# print(df.info())

# Question 21:Identify which column has missing values
df.isna().any()

# Question 22:Find Total number of rows and columns in dataset
total_rows=len(df)
print("Total rows:",total_rows)
total_columns=len(df.columns)
print("Total rows:",total_columns)

# Question 23:Find Which column has the most missing values
most_missing_value=df.isna().sum()
print(most_missing_value)
import numpy as np
import pandas as pd
df=pd.read_csv(r"anime.csv",encoding="latin1")
print(df)

# Basic Exploration 
'''Q1.Show:First 10 rows
Q2.Find:Total number of anime
Q3.Check:All column names
Q4.Check:Data types of each column'''

# Question 1
# first10_rows=df.head(10)
# print(first10_rows)

# Question  2
# total_anime=len(df["name"])
# print("total anime:",total_anime)

# Question 3
# column_name=df.columns
# print(column_name)

# Question 4
# datatype_column=df.dtypes
# print(datatype_column)

# Cleaning 
'''Q5.Find:Missing values in each column
Q6.Clean:Replace unknown ratings (NaN)
Q7.Convert:episodes column into numeric
(Hint: some values are "Unknown")'''

# Question 5
# find_missing_value=df.isna().sum()
# print(find_missing_value)

# Question 6
# df["rating"] = df["rating"].fillna(df["rating"].mean())

# Question 7
# df["episodes"] = df["episodes"].replace("Unknown", pd.NA)
# df["episodes"] = pd.to_numeric(df["episodes"])

# Analysis 
'''Q8.Find:Top 10 highest rated anime
Q9.Find:Most popular anime (based on members)
Q10.Find:Average rating of all anime'''

# Question 8
top_highest_rate_anime=df.sort_values(by="rating",ascending=False)[["name","rating"]].head(10)
print("Top highest rated anime")
print(top_highest_rate_anime)

# Question 9
most_popular_anime=df.sort_values(by="members",ascending=False)[["name","members"]].head(10)
print("Most popular anime")
print(most_popular_anime)

# Question 10
average_rate_anime=(df["rating"]).mean()
print(average_rate_anime)
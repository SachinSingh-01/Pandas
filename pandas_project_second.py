import numpy as np
import pandas as pd
df=pd.read_csv(r"netflix_titles.csv",encoding="latin1")
print(df)
# Data Understanding 
'''Q1.Find:Total number of Movies vs TV Shows
Q2.Find:Top 10 countries producing most content
Q3.Find:Year-wise content added trend
(Hint: use date_added)'''
# Question 1
# total_movies_TV_shows=df["type"].value_counts()
# print(total_movies_TV_shows)

# Question 2
# top_most_content=df["country"].value_counts().head(10)
# print(top_most_content)

# Question 3
df["date_added"]=pd.to_datetime(df["date_added"],errors="coerce")
year_trend=df["date_added"].dt.year.value_counts().sort_values()
print(year_trend)

# Data Cleaning + Transformation
'''Q4.Clean:date_added column → convert to datetime
Then extract:
year
month
Q5.Clean:duration column
Extract:
numeric value
unit (minutes / seasons)
Q6.Handle:Missing values in country, rating, director'''
# Question 4
# df["datetime"]=df.to_datetime(df["date_added"])
# print(df)

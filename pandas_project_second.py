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
# df["date_added"]=pd.to_datetime(df["date_added"],errors="coerce")
# year_trend=df["date_added"].dt.year.value_counts().sort_values()
# print(year_trend)

# Data Cleaning + Transformation
'''Q4.Clean:date_added column → convert to datetime
Then extract:
year
month
Q5.Clean:duration column
Extract:
numeric value unit (minutes / seasons)
Q6.Handle:Missing values in country, rating, director'''
# Question 4
# df["date_added"]=pd.to_datetime(df["date_added"],errors="coerce")
# extract_year=df["date_added"].dt.year.sort_values().value_counts()
# extract_month=df["date_added"].dt.month.sort_values().value_counts()
# print(extract_year)
# print(extract_month)

# Question 5
# df["duration_num"] = df["duration"].str.extract(r"(\d+)")
# df["duration_num"] = pd.to_numeric(df["duration_num"],errors="coerce")
# df["duration_unit"] = df["duration"].str.extract(r"([a-zA-Z]+)")
# print(df)

# Question 6
# df["rating"]=df["rating"].fillna(df["rating"].mode()[0])
# df["country"] = df["country"].fillna("Unknown")
# df["director"]=df["director"].fillna("Not available")
# print(df.isna().sum())

# Analytical Thinking
'''Q7.Find:Which year had the highest content addition
Q8.Find:Average duration of Movies
Q9.Find:Distribution of ratings (TV-MA, PG, etc.)'''

# Question 7
# df["date_added"]=pd.to_datetime(df["date_added"],errors="coerce")
# df["year"]=df["date_added"].dt.year
# year_count=df["year"].value_counts()
# high_content_addition=year_count.idxmax()
# print(high_content_addition)

# Question 8
# df["duration_num"] = df["duration"].str.extract(r"(\d+)")
# df["duration_num"] = pd.to_numeric(df["duration_num"], errors="coerce")
# average_duration_movies=df[df["type"]=="Movie"]["duration_num"].mean()
# print(average_duration_movies)

# Question 9
# dis_rating=df["rating"].value_counts()
# print(dis_rating)

# Advanced Analysis 
'''Q10.Find:Top 5 directors with most content
Q11.Find:Top 5 actors appearing most
(Hint: cast column → multiple values)
Q12.Find:Which country produces highest rated content'''

# Question 10
# df["director"]=df["director"].fillna("Not available")
# df["director"]=df["director"].str.split(",")
# df=df.explode("director")
# df = df.reset_index(drop=True)
# df["director"]=df["director"].str.strip()
# top_director=df["director"].value_counts().head(5)
# print(top_director)

# Question 11
# df = df.dropna(subset=["cast"])
# df["cast"]=df["cast"].str.split(",")
# df=df.explode("cast")
# df["cast"]=df["cast"].str.strip()
# df = df.reset_index(drop=True)
# top_appear_actor=df["cast"].value_counts().head(5)
# print(top_appear_actor)

# Question 12
# df["country"]=df["country"].fillna("Not present")
# df["country"]=df["country"].str.split(",")
# df=df.explode("country")
# df["country"]=df["country"].str.strip()
# df = df.reset_index(drop=True)
# country_high_content=df["country"].value_counts()
# print(country_high_content)

# Business Insight 
'''Q13.Answer:
Is Netflix focusing more on Movies or TV Shows?
Justify using data
Q14.Find:
Trend:Is Netflix adding more content in recent years?
Q15.Find:Which genre/type is growing fastest'''

# Question 13
# counts=df["type"].value_counts()
# movies_count=counts["Movie"]
# tvshow_count=counts["TV Show"]
# print(movies_count)
# print(tvshow_count)
# if (movies_count)>(tvshow_count):
#     print("Movie is more")
# else:
#     print("Tv_show is more")
# grouping=df.groupby(["release_year","type"]).size()
# print(grouping)
# print("Movies count is significantly higher than TV Shows, indicating that Netflix focuses more on Movies. However, recent trends show TV Shows are also increasing.")

# Question 14
# df["date_added"]=pd.to_datetime(df["date_added"],errors="coerce")
# df["year"]=df["date_added"].dt.year
# year_count=df["year"].value_counts().sort_index()
# print(year_count)

# Question 15
# df["listed_in"]=df["listed_in"].fillna("unknown")
# df["listed_in"]=df["listed_in"].str.split(",")
# df=df.explode("listed_in")
# df["listed_in"]=df["listed_in"].str.strip()
# df["date_added"]=pd.to_datetime(df["date_added"],errors="coerce")
# df["year"]=df["date_added"].dt.year
# genre_count=df.groupby(["year","listed_in"]).size().reset_index(name="count")
# print(genre_count)

# PRO LEVEL 
'''Q16.Create:New column → content_age
current_year - release_year
Then analyze:Are newer or older shows more common?
Q17.Build:Recommendation logic:
Find top content for:
new users
based on rating + recent release
Q18.Segment:Content into:
Short
Medium
Long
Based on duration'''

# Question 16
df["content_age"]=2026-(df["release_year"])
print(df)
df["age_group"]=df["content_age"].apply(lambda x: "new" if  x<=5 else "old")
count=df["age_group"].value_counts()
print(count)
print("After analysing the dataset the old_age people more than the new_ager")

# Question 17

# # Question 18
df["duration_num"] = df["duration"].str.extract(r"(\d+)").astype(float)
def segment(x):
    if x<60:
        return "Short"
    elif x<=120:
        return "Medium"
    else: 
        return "Long"
count=df["duration_category"]=df["duration_num"].apply(segment)
counting=df["duration_category"].value_counts()
print(counting)
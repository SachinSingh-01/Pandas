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
# top_highest_rate_anime=df.sort_values(by="rating",ascending=False)[["name","rating"]].head(10)
# print("Top highest rated anime")
# print(top_highest_rate_anime)

# Question 9
# most_popular_anime=df.sort_values(by="members",ascending=False)[["name","members"]].head(10)
# print("Most popular anime")
# print(most_popular_anime)

# Question 10
# average_rate_anime=(df["rating"]).mean()
# print(average_rate_anime)

# Grouping
'''Q11.Find:Average rating by type (TV, Movie, OVA)
Q12.Find:Total number of anime per type
Q13.Find:Average number of episodes per type'''

# Question 11
# average_rating=df.groupby("type")["rating"].mean()
# print(average_rating)

# Question 12
# total_no_anime=df.groupby("type")["name"].count()
# print(total_no_anime)

# Question 13
# total_episodes=df.groupby("type")["episodes"].mean()
# print(total_episodes)

# Genre Analysis
'''Q14.Find:Most common genre
(Hint: genre column has multiple values)
Q15.Find:Highest rated genre'''

# Question 14
# df["genre"]=df["genre"].str.split(", ")
# explode=df.explode("genre")
# most_common_genre=explode["genre"].value_counts().idxmax()
# print(most_common_genre)

# Question 15
# df["genre"]=df["genre"].str.split(", ")
# explode=df.explode("genre")
# highest_rate_genre=explode.groupby("genre")["rating"].mean().idxmax()
# print(highest_rate_genre)

# Real Business Thinking 
'''Q16.Which type of anime:has highest engagement (members)?
Q17.Find:Top 5 anime with:
high rating
high members
Q18.Find:Relationship:Do more episodes → higher rating?'''

# Question 16
# high_type_member=df.groupby("type")["members"].sum().sort_values(ascending=False)
# print(high_type_member)

# Question 17
# top_rating_member=df.sort_values(by=["rating","members"],ascending=False).head(5)
# print(top_rating_member)

# Question 18
# df["episodes"] = pd.to_numeric(df["episodes"], errors="coerce")
# relation_episodes_rating=df["episodes"].corr(df["rating"])
# print(relation_episodes_rating)

# Pro Level 
'''Q19.Create new column:"popularity_score"
Formula:rating x members
Q20.Find:Top 10 anime based on popularity_score'''

# Question 19
# df["popularity_score"]=df["rating"]*df["members"]
# print(df)

# Question 20
# top_best_anime_pop_score=df.sort_values(by="popularity_score",ascending=False).head(10)
# print(top_best_anime_pop_score)
# Data Understanding 
'''Q1.Find:Total number of anime in each type (TV, Movie, OVA)
Q2.Find:Percentage of missing values in each column
Q3.Find:Top 5 most common genres
(Hint: genre column has multiple values)'''

# Question 1
# total_anime_type=df.groupby("type").size().head(5)
# print(total_anime_type)

# Question 2
# percent_miss_value=df.isnull().sum()*100/len(df)
# print(percent_miss_value)
# print(total_anime_type)

# Question 3
# most_common_genres=df["genre"].str.split(", ").explode().value_counts().head(5)
# print(most_common_genres)

# Business Insights
'''Q4.Which type of anime:
has highest average rating
and highest total members
Compare both (important insight)
Q5.Find:Top 10 anime which are:
high rating
high members
(Not just one column → combine thinking)'''

# Question 4
high_rating_members=df.groupby("type").agg({
    "rating": "mean",
    "members": "sum"
})
print(high_rating_members)

# Question 5
df["score"]=df["rating"]*df["members"]
top_anime_rate_members=df.sort_values(by="score",ascending=False)[["name","rating","members"]].head(10)
print(top_anime_rate_members)

# Question 6

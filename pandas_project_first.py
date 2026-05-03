import numpy as np
import pandas as pd
df=pd.read_csv(r"netflix_titles.csv",encoding="latin1")

# phase-1
print(df.head())
print(df.info())
print(df.dtypes)

total_rows=df.shape[0]
total_column=df.shape[1]
print("Total rows:",total_rows)
print("Total column:",total_column)

mising_column_value=df.isnull().sum()
print(mising_column_value)

print(df.dtypes)

# Handling missing value
df["director"]=df["director"].fillna("Not available")
df["country"]=df["country"].fillna("Unknown")
df["rating"]=df["rating"].mode()[0]


# Clean duration
df["duration_num"]=df["duration"].str.extract(r"(\d+)").astype(float)
print(df)


count=df["type"].value_counts()
movies_count=count["Movie"]
tv_count=count["TV Show"]
print(movies_count)
print(tv_count)
if movies_count>tv_count:
    print("Movies is more than tv_show")
else:
    print("TV show is more than movies")

# df["date_added"]=pd.to_datetime(["date_added"],errors="coerce")
# df["year_added"]=df["date_added"].dt.year
# grouping=df.groupby(by="year_added",ascending=False).size()
# print(grouping)


# df["country"]=df["country"].fillna("Not available")
# df["country"]=df["country"].str.split(",")
# df=df.explode("country")
# df=df.reset_index(drop=True)
# df["country"]=df["country"].str.strip()
# top_country=df["country"].value_counts().head(20)
# print(top_country)

# df["listed_in"]=df["listed_in"].fillna("Not available")
# df["listed_in"]=df["listed_in"].str.split(",")
# df=df.explode("listed_in")
# df=df.reset_index(drop=True)
# df["listed_in"]=df["listed_in"].str.strip()
# top_genre=df["listed_in"].value_counts().head(10)
# print("Top genre")
# print(top_genre)

df["duration_num"]=df["duration"].str.extract(r"(\d+)")
df["duration_num"]=pd.to_numeric(df["duration_num"],errors="coerce")
avg_dur_movies=df[df["type"]=="Movie"]["duration_num"].mean()
print(avg_dur_movies)
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


import pandas as pd

df = pd.read_csv("datasets/IMDBdata_MainData_poster_refresh.csv")

# 1-) Show information about csv.
result = df

# 2-) First 5 record in csv
result = df.head(5)

# 3-) First 10 record in csv
result = df.head(10)

# 4-) Last 5 record in csv
result = df.tail(5)

# 5-) Last 10 record in csv
result = df.tail(10)

# 6-) Just show title column.
result = df["title"]

# 7-)Just show first 5 record include title column.
result = df["title"].head()

# 8-)Just  show first 5 record include title and rating column.
result = df[["title", "imdbrating"]].head(5)

# 9-)Just  show last 7 record include title and rating column.
result = df[["title", "imdbrating"]].tail(7)

# 10-)Just show second 5 record include title and rating column.
result = df[5:10][["title", "imdbrating"]].head(5)

# 11-) Just show first 50 record include title and rating column but only imdb rating bigger than 8.0
result = df.query("imdbrating >= 8.0")[["title", "imdbrating"]].head(50)

# 12-) Just show title and year where release date between 2014-2015
result = df.query("year >=2014 & year <=2015")[["title", "year"]]

# 13-) Just show title, imdb votes and imdb rating where imdb votes bigger than 100.000 or imdb rating between 8 and 9.
df["imdbvotes"] = df["imdbvotes"].str.replace(",", "")
df["imdbvotes"] = pd.to_numeric(df["imdbvotes"])
result = df.query("(imdbvotes >= 100000) | ((imdbrating >= 8.0) & (imdbrating <=9.0))")[
    ["title", "imdbvotes", "imdbrating"]]
print(result)

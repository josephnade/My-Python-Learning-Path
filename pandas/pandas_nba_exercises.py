import pandas as pd

df = pd.read_csv("datasets/nba.csv")
result = df

# 1-) Show first 10 column.
result = df.head(10)

# 2-) How many record that nba.csv have ?
result = len(df.index)

# 3-) What is the average of all players' salary ?
result = df["Salary"].mean()

# 4-) What is the maximum salary of nba players ?
result = df["Salary"].max()

# 5-) Who has the highest salary ?
result = df[df["Salary"] == df["Salary"].max()]["Name"].iloc[0]

# 6-) Show name and their teams that has 20 - 25 ages but teams order must be decreasing.
result = df.query("Age >= 20 & Age <=25")[["Name", "Team"]].sort_values("Team", ascending=False)

# 7-) What is the team which "James Johnson" plays ?
result = df[df["Name"] == "James Johnson"]["Team"].iloc[0]

# 8-) What is the players' salary average according to teams ?
result = df.groupby("Team").mean()["Salary"]


# 9-) How many team are there ?
result = len(df["Team"].unique())


# 10-) How many players play in each team ?
result = df["Team"].value_counts()

# 11-) Which players' name contain "and" ?
df.dropna(inplace=True)
result = df[df["Name"].str.contains("and")]


print(result)
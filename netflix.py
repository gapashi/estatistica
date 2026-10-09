import pandas as pd

df = pd.read_csv('netflix_titles.csv')
# print(df.describe())
# print(df.info())

df = df.drop_duplicates()
df = df.dropna()
print(df)
print(df.info())
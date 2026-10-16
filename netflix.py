import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('netflix_titles.csv')
# print(df.describe())
# print(df.info())

df = df.drop_duplicates()
df = df.dropna()
print(df)
print(df.info())

sns.boxplot(x=df["release_year"])
plt.title("Boxplot de Lançamentos")
plt.show()
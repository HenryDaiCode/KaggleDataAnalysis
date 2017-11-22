#Is there a relationship between Genre and Year?
import pandas as pd
import scipy.stats
df = pd.read_csv(r"D:\Documents\Python\Kaggle\gamesales.csv")
df = df[df.Year > 1994]
df = df[df.Year < 2017]
print(scipy.stats.chisquare(df.loc[:, "Genre"].value_counts()))
print(scipy.stats.chisquare(df.loc[:, "Year"].value_counts()))
contingencyTable = pd.crosstab(df.loc[:, "Genre"], df.loc[:, "Year"])
print(scipy.stats.chi2_contingency(contingencyTable))
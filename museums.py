import pandas as pd
import matplotlib.pyplot as plt

#Replace with your filepath
df = pd.read_csv("D:\Documents\Python\Kaggle\museums.csv", low_memory = False, encoding="latin1")
numrows = df.shape[0]

#Removing any museums without revenue or income information
cleandf = df
cleandf = cleandf.dropna(subset=["Income", "Revenue"], how = "any")
print("{} museums without revenue or income information removed from a total of {}".format(numrows - cleandf.shape[0], numrows))

#Storing the number of rows at the start
numrows = cleandf.shape[0]

#Removing museums with zero income
#cleandf = cleandf[cleandf.Income != 0]
#print("{} museums with zero income from a total of {}".format(numrows - cleandf.shape[0], numrows))
#numrows = cleandf.shape[0]

#Removing outliers
cleandf = cleandf[cleandf.Income >= 10000]
print("{} museums with income less than 10000 removed from a total of {}".format(numrows - cleandf.shape[0], numrows))
numrows = cleandf.shape[0]

cleandf = cleandf[cleandf.Income <= (10 ** 6)]
print("{} museums with income greater than 10^6 removed from a total of {}".format(numrows - cleandf.shape[0], numrows))

#print(cleandf.describe())
income = cleandf["Income"]
#print(income)
(n, bins, patches) = plt.hist(income)
plt.title("Distribution of museums with income between \$10000 and \$1000000")
#print(bins)
#print(n)
plt.show()
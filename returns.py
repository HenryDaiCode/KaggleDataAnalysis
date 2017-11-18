from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt

start_date = "2010-01-01"
end_date = "2017-11-17"

adjclose = data.DataReader("^gspc", "yahoo", start_date, end_date)["Adj Close"]
plt.figure(figsize=(20,10))
returns = adjclose.pct_change(1)
returns.plot(grid = True)
plt.show()
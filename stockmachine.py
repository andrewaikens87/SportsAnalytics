import pandas as pd

# Importing data from .csv to DataFrame
df=pd.read_csv('/StockMachine/data_stocks.csv', sep=',',header=None)

# Data is in an array of arrays
# [['DATE' 'SP500' 'NASDAQ.AAL' ... 'NYSE.YUM' 'NYSE.ZBH' 'NYSE.ZTS']
# ['1491226200' '2363.6101' '42.33' ... '63.86' '122' '53.35']
# ['1491226260' '2364.1001' '42.36' ... '63.74' '121.77' '53.35']
# ...
# [1504209480 2470.03 44.74 ... 76.88 114.31 62.685]
# [1504209540 2471.49 44.71 ... 76.83 114.23 62.6301]
# [1504209600 2471.49 44.74 ... 76.81 114.28 62.68]]
data = df.values

# To convert to dictionary
# df2 = pd.DataFrame(data, columns = df.columns)
# df2.to_dict(orient='records')

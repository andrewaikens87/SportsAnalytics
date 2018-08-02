import pandas as pd

# Grabbing headers as an Index (immutable ndarray implementing an ordered, sliceable set).
# col_names.values to get column names as just array
col_names = pd.read_csv('~/StockMachine/data_stocks.csv', nrows=0).columns

# Specifying dtype as 'float64' for all columns other than 'DATE'
types_dict = {}
types_dict.update({col: 'float64' for col in col_names if col != 'DATE'})

# Importing data from .csv to DataFrame with specified dtypes
df = pd.read_csv('~/StockMachine/data_stocks.csv', dtype=types_dict)

# Convert unix time to readable date by casting dates to 'datetime64[ns]' dtype
df['DATE'] = pd.to_datetime(df['DATE'],unit='s')

# Data (without col_names) as numpy.ndarray.
# Dates in form Timestamp('2017-04-03 13:30:00') due to Numpy representation of DataFrame
data = df.values
print(data)

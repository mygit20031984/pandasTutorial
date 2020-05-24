import pandas as pd

#1# Read CSV - With HEader#
#df = pd.read_csv('stock_data_withheader.csv.csv')

#2# Read CSV - Additional Header#
#df = pd.read_csv('stock_data_additionalheader.csv', header = 1)
#df = pd.read_csv('stock_data_additionalheader.csv', skiprows = 1)


#3# Read CSV - No Header#
df = pd.read_csv('stock_data_withoutheader.csv', header = None, names=['tickers','eps','revenues','price','people'])
print(df)
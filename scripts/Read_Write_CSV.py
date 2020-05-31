import pandas as pd

#1# Read CSV - With HEader#
#df = pd.read_csv('stock_data_withheader.csv.csv')

#2# Read CSV - Additional Header#
#df = pd.read_csv('stock_data_additionalheader.csv', header = 1)
#df = pd.read_csv('stock_data_additionalheader.csv', skiprows = 1)

#3# Read CSV - No Header#
#df = pd.read_csv('stock_data_withoutheader.csv', header = None, names=['tickers','eps','revenues','price','people'])
#print(df)

#4# Read few rows in CSV#
#df = pd.read_csv('stock_data_withheader.csv', nrows = 3)
#print(df)

#5# NA Values handling#
#df = pd.read_csv('stock_data_withheader.csv', na_values=['not available', 'n.a.'])
#print(df)

df = pd.read_csv('../stock_data_withheader.csv', na_values={
    'eps' : ['not available', 'n.a.'],
    'revenues' : ['not available', 'n.a.', -1],
    'price' : ['not available', 'n.a.'],
    'people' : ['not available', 'n.a.']
    })
print(df)
#df.to_csv('new_csv.csv' , index = False)

#6# specific Columns#
#df.to_csv('new_csv.csv' , index = False, columns = ['tickers', 'eps'])

#7# skip header#
df.to_csv('new_csv.csv' , index = False, header=False)


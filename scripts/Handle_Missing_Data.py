import pandas as pd

df = pd.read_csv('weather_file.csv', parse_dates=['day'])
df.set_index('day',inplace=True)

#1# Fill NA
#df1 = df.fillna(0)

#2# Fill NA for different columns with different values
# df1 = df.fillna({
#     'temperature' : 0,
#     'windspeed' : 0,
#     'event' : 'no event'
#     })

#3# Forward Fill
#df1 = df.fillna(method='ffill')

#4# Backword Fill
#df1 = df.fillna(method='bfill')

#5# Axis Fill, We also use "limit" method to limit fill.
#df1 = df.fillna(method='bfill' , axis='columns')

#6# Interpolation
#df1 = df.interpolate(method='time')

#7# drop NA
#df1 = df.dropna(how='all')
#df1 = df.dropna(thresh=2)
#print(df1)

#8# re-indexing
dt = pd.date_range('01-01-2020', '01-11-2020')
idx = pd.DatetimeIndex(dt)
df = df.reindex(idx)
print(df)

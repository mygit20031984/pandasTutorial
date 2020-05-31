import pandas as pd

weather_data = {
    'Day' : ['1/1/2020','1/2/2020','1/3/2020','1/4/2020','1/5/2020',],
    'Temperature' : [23,32,43,23,38],
    'Windspeed' : [3,4,6,3,8],
    'Event' : ['rain', 'sunny', 'snow','sunny','rain']}
df = pd.DataFrame(weather_data)
# print(df)
# shape = df.shape
# print('DF Shape is :' , shape)
# rows, columns = df.shape
# print('DF Rows and Columns are %s and %s'%(rows, columns))
# print('DF head : \n', df.head(2))
# print('DF tail : \n', df.tail(2))
# print('DF slicing : \n', df[2:5])
# print('DF step : \n', df[::2])
# print('DF columns : \n', df['Temperature'])
#print(type(df['Event']))
#print(df[['Event', 'Day']])
# print('Max Temperature is: ', df['Temperature'].max())
# print('Min Temperature is: ', df['Temperature'].min())
# print('Standard deviation Temperature is: ', df['Temperature'].std())
# print('Describe Temperature is: \n', df.describe())
# print('Records with Temperature greater than 32 are: \n', df[df['Temperature'] >= 32])
# print('Records with Temperature greater than 32 are: \n', df[df['Temperature'] == df['Temperature'].max()])
#print('Records with Temperature greater than 32 are: \n', df[df['Temperature'] == df.Temperature.max()])
#print('Records with Temperature greater than 32 are: \n', df[['Temperature', 'Day']][df['Temperature'] == df.Temperature.max()])
#Pandas series operations

df.set_index('Day', inplace=True)
print(df)
# print(df.loc['1/4/2020'])
df.reset_index(inplace=True)
print(df)

import pandas as pd

df = pd.read_csv('D:\\Ashu\\python\\Pandas\\weather.csv')
#print(df)
max_t = df['Temperature'].max()
print('Max Temperature is: %s ' %(max_t))

date_rain = df['EST'][df['Events'] == 'Rain']
print('\nDate on which it Rained are: \n %s' %(date_rain))

df.fillna(0, inplace=True)
avg_windspeed = df['WindspeedMPH'].mean()
print('Avg Windspeed is: %s ' %(avg_windspeed))
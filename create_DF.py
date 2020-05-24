import pandas as pd

#1# Read CSV#
# df = pd.read_csv('D:\\Ashu\\python\\Pandas\\weather1.csv')

#2# READ Excel#
#df = pd.read_excel("D:\\Ashu\\python\\Pandas\\weather_excel.xlsx", "Sheet1")

#3# Read Dictionary#
# weather_data = {
#     'Day' : ['1/1/2020','1/2/2020','1/3/2020','1/4/2020','1/5/2020',],
#     'Temperature' : [23,32,43,23,38],
#     'Windspeed' : [3,4,6,3,8],
#     'Event' : ['rain', 'sunny', 'snow','sunny','rain']}
# df = pd.DataFrame(weather_data)

#4# Tuple List
# weather_data = [
#     ('1/1/2020',23,4,'Rain'),
#     ('1/2/2020',34,7,'Rain'),
#     ('1/3/2020',29,3,'Snow')
# ]
# df = pd.DataFrame(weather_data, columns=['Day','Temperature','Windspeed','Event'])

#5# List of Dictionaries
weather_data = [
    {'Day': '1/1/2020','Temperature':'23','Windspeed':'8', 'Event': 'Rain'},
    {'Day': '1/2/2020','Temperature':'43','Windspeed':'22', 'Event': 'Windy'},
    {'Day': '1/3/2020','Temperature':'33','Windspeed':'18', 'Event': 'Snow'},
]
df = pd.DataFrame(weather_data)
print(df)
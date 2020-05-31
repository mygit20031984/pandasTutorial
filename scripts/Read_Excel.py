import pandas as pd
#from openpyxl.workbook import Workbook

#df = pd.read_excel('Excel_stock_data.xlsx' , 'Sheet1')
#print(df)

#1# Converter:
#
# def convert_people_cell(cell):
#     if cell == 'n.a.':
#         return  'Ashutosh Kulkarni'
#     return cell
# df = pd.read_excel('Excel_stock_data.xlsx' , 'Sheet1', converters={
#     'people' : convert_people_cell
# })
# print(df)
# df.to_excel('new_excel_noheader_index.xlsx', sheet_name='Sheet1', index=False, header=False, startrow=2,startcol=5)

#2# Writting 2 dataframes to single excel in 2 different sheets
weather_data = {
    'Day' : ['1/1/2020','1/2/2020','1/3/2020','1/4/2020','1/5/2020',],
    'Temperature' : [23,32,43,23,38],
    'Windspeed' : [3,4,6,3,8],
    'Event' : ['rain', 'sunny', 'snow','sunny','rain']}
df1 = pd.DataFrame(weather_data)


stocks_data = {
    'ticker' : ['GOOGL','WMT','MSFT'],
    'price' : [453,121,675],
    'pe' : [30.12,14.87,30.8],
    'eps' : [27.82,30.12,41.12]}
df2 = pd.DataFrame(stocks_data)

with pd.ExcelWriter('../new_excel_multisheet.xlsx') as writer:
    df1.to_excel(writer, sheet_name='weather_data', index=False, header=False, startrow=2,startcol=5)
    df2.to_excel(writer, sheet_name='stocks_data')
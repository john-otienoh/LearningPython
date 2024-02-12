import csv
weather_data = list(csv.DictReader(open('weather.csv')))
day_list=[]
for i in weather_data:
    day_list.append(i['day'])
print(day_list)
print(weather_data)

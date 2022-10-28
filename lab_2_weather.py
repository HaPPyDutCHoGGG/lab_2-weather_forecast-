#weather_forecast
import requests as rq;

city = 'Moscow,RU';
appid = '8858bc3ed6fdb405491ff578c5c59bb1';

#region actual_Weather
'''
res = rq.get("http://api.openweathermap.org/data/2.5/weather",
             params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid}
    );
data = res.json();

print("Город:", city);
print("Погодные условия:", data['weather'][0]['description']);
print("Температура:", data['main']['temp']);
print("Минимальная температура:", data['main']['temp_min']);
print("Максимальная температура", data['main']['temp_max']);

print("visibility:", data['visibility']); #exercize
print("wind:", data['wind']['speed']);
'''
#endregion

#region Forecast

res = rq.get("http://api.openweathermap.org/data/2.5/forecast",
             params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid}
    );
data = res.json();

print("forecast 4 week:-----------")


'''
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <", i['weather'][0]['description'], ">")
    print("____________________________")
'''


print('forecast 4 week');
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']),
          "> \r\nПогодные условия <", i['weather'][0]['description'], ">",
          "> \r\nVisibility <", i['visibility'], ">",
          #"> \r\nWind <", i['wind'][0]['speed'], ">"
          );

    print('____________');
  
#endregion

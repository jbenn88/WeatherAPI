import requests
from pprint import pprint


def main():

    city = input('Enter the city you would like weather for:')
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=be13590b8e6a20e144790c1780bfcc11&units=imperial')
    weather = response.json()
    # pprint for print json obj to see structure
    #pprint(weather)
    print("The current weather for", weather['name'] + ":")
    print("Temperature:", weather['main']['temp'])
    print("Weather description:", weather['weather'][0]['description'])
    if("rain" in weather['weather'][0]['description']):
        print("Rain duration and amount:", weather['rain'])

if __name__ == '__main__':
    main()
import requests

city = input("Enter city: ")
var_request = requests.get( f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

print("Weather: " + var_request.json()['weather'][0]['description'])
print("Temperature: " + str(var_request.json()['main']['temp']) + "C°")
print("Feels Like: " + str(var_request.json()['main']['feels_like']) + "C°")
print("Min: " + str(var_request.json()['main']['temp_min']) + "C°")
print("Max: " + str(var_request.json()['main']['temp_max']) + "C°")
#print(var_request.status_code)
#print(var_request.json())

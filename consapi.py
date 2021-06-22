import requests

ciudad = input("Ingrese su ciudad: ")

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=cb01650f5633a991ad1e1833aee70aab&units=metric'.format(ciudad)

res = requests.get(url)

data = res.json()
description = data['weather'][0]['description']
vel_viento = data['wind']['speed']
temp = data['main']['temp']
latitud = data['coord']['lat']
longitud = data['coord']['lon']

print('Descripcion : {}'.format(description))
print('Velocidad del viento : {} m/s'.format(vel_viento))
print('Temperatura : {} grados celcius'.format(temp))
print('Latitud : {}'.format(latitud))
print('Longitud : {}'.format(longitud))
print("Script desarrollado por Facundo Pinget y Lautaro Silva")
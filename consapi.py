import requests

ciudad = input("Ingrese su ciudad: ")

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=cb01650f5633a991ad1e1833aee70aab&units=metric'.format(ciudad)

res = requests.get(url)

data = res.json()

temp = data['main']['temp']
vel_viento = data['wind']['speed']
latitud = data['coord']['lat']
longitud = data['coord']['lon']
description = data['weather'][0]['description']

print('Temperatura : {} grados celcius'.format(temp))
print('Velocidad del viento : {} m/s'.format(vel_viento))
print('Latitud : {}'.format(latitud))
print('Longitud : {}'.format(longitud))
print('Descripcion : {}'.format(description))
print("Script desarrollado por Facundo Pinget y Lautaro Silva")
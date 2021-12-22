"""JSON-- JavaScript Object Notation is a format for structuring data. 
It is mainly used for storing and transferring data between the browser and the server."""

"""API-- An API, or Application Programming Interface, is a server 
that you can use to retrieve and send data to using code """

import requests
from pprint import pprint
city= input("Enter city name: ")
api = "93c52a6f3f6acb32c2c5fed6ec1500a3"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
weather = requests.get(url).json() 
pprint(weather)


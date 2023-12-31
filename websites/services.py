import requests

def get_API_DATA(lat, lon, key, what_type):
    url = "https://api.weatherapi.com/v1" 
    lat = lat
    lon = lon
    key = key
    what_type = what_type
    url = url + what_type + "?key=" + key + "&q=" + lat + "," + lon
    r = requests.get(url)
    books = r.json()
    books_list = {'books':books['results']}
    return books_list
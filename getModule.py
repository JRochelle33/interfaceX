import requests

def getter(endPoint):
    baseURL = "https://api.spacexdata.com/v3/"

    r = requests.get(baseURL + endPoint)
    return r


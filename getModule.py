import requests

def getter(lvlOne, lvlTwo):
    baseURL = "https://api.spacexdata.com/v3/"
    if len(lvlTwo) == 1:
        if lvlTwo[0] == 'All Available':
            r = requests.get(baseURL + lvlOne)
            return r
        else:
            r = requests.get(baseURL + lvlOne + "/" + lvlTwo[0])
            return r
    else:
        r = requests.get(baseURL + lvlOne + "/" + lvlTwo[1])
        return r

import json
import getModule

levelOne = {
    "1": "Capsules",
    "2": "Cores",
    "3": "Dragons",
    "4": "History",
    "5": "Info",
    "6": "Landing Pads",
    "7": "Launches",
    "8": "Missions",
    "9": "Payloads",
    "10": "Rockets",
    "11": "Roadster",
    "12": "Ships",
    "q" : "quit"
}

def options():

    for key, value in levelOne.items() :
        print (key,":", value)

    userSelect = input("What endpoint would you like? \n")

    if userSelect == "q":
        return

    if userSelect in levelOne:
        endPoint = levelOne[userSelect]
        data = getModule.getter(endPoint).json()
        print(data)
        return levelOne[userSelect]
    else:
        print ("***Please enter the number of selection***")
        options()

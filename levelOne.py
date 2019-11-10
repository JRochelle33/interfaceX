import json
import getModule

primaryMenu = {
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

def categories():

    for key, value in primaryMenu.items() :
        print (key,":", value)

    userSelect = input("\n What category would you like? \n")

    if userSelect == "q":
        return
    elif primaryMenu[userSelect] == "Landing Pads":
        primaryMenu[userSelect] = "Landpads"
    elif userSelect in primaryMenu:
        return primaryMenu[userSelect]
    else:
        print ("***Please enter the number of selection***")
        categories()

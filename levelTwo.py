import getModule

secondaryMenu = {
    'Capsules' : {'1': 'All Available', '2': 'Serial', '3': 'Past', '4': 'Upcoming', '5': 'Return'},
    'Cores' : {'1': 'All Available', '2': 'Serial', '3': 'Past', '4': 'Upcoming', '5': 'Return'},
    'Dragons' : {'1': 'All Available', '2': 'ID', '3': 'Return'},
    'History' : {'1': 'All Available', '2': 'ID', '3': 'Return'},
    'Info' : {'1': 'Company', '2': 'API', '3': 'Return'},
    'Landpads' : {'1': 'All Available', '2': 'ID', '3': 'Return'},
    'Launches' : {'1': 'All Available', '2' : 'Flight Number', '3': 'Past', 
                  '4': 'Upcoming', '5': 'Latest', '6': 'Next', '7': 'Return'},
    'Launchpads' : {'1': 'All Available', '2': 'Site ID', '3': 'Return'},
    'Missions' : {'1': 'All Available', '2': 'Mission ID', '3': 'Return'},
    'Payloads' : {'1': 'All Available', '2': 'Payload ID', '3': 'Return'},
    'Rockets' : {'1': 'All Available', '2': 'Rocket ID', '3': 'Return'},
    'Roadster' : {'1': 'All Available', '2': 'Return'},
    'Ships' : {'1': 'All Available', '2': 'Ship ID', '3': 'Return'}
}

hasInput = ['Serial', 'ID', 'Flight Number', 'Site ID', 'Mission ID', 'Payload ID', 'Rocket ID', 'Ship ID']

def subCategories(lvlOne):
    if lvlOne in secondaryMenu:
        for key, value in secondaryMenu[lvlOne].items() :
            print (key,":", value)
    else:
        return
    
    userSelect = input("\n How would you like to continue? \n")
    userSelected = secondaryMenu[lvlOne][userSelect]

    if userSelected in hasInput:
        idValue = input("\n Enter ID \n")
        lvlTwo = [userSelected, idValue]
        return lvlTwo
    else:
        lvlTwo = [userSelected]
        return lvlTwo
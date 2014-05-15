#Dice roll program
#Rolls a dice then shows the face

import random, time #Include some libraries

strings = ["- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n", "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n", "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n", "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n", "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n", "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"]
#Create a list of strings

def roll(): #Create a function that rolls a dice
    print("Rolling.....")
    roll = random.randint(1, 6)
    return roll


def show_dice(roll): #Define a function that prints the dice face
    print(strings[roll-1])

rolled = -1 #Initialize rolled
while rolled != 6: #While they did not roll a 6
    input("Press Enter to roll") #Wait for the user to press 'Enter'
    rolled = roll() #Roll the dice
    time.sleep(1) #Wait a second
    show_dice(rolled) #Show the face

#Corrected introductory comment
#Replaced ';' with a ',' and a ' '
#Fixed casing and missing parentheses.
#Fixed typos and spelling errors

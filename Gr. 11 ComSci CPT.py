#import random library for later use
import random

#set variable(s)
done = False

#opens save file, reads each line, removes whitespace and sets values according to save file (0, False, False, False, by default)
save_file = open("save_file.txt", "r")
current_room = int(save_file.readline().strip())
south_key = save_file.readline().strip()
north_key1 = save_file.readline().strip()
north_key2 = save_file.readline().strip()
save_file.close()

#converts values stored in key variables from strings to booleans
if south_key == "True":
    south_key = True
else:
    south_key = False

if north_key1 == "True":
    north_key1 = True
else:
    north_key1 = False

if north_key2 == "True":
    north_key2 = True
else:
    north_key2 = False

#Functions are defined (more in each function's docstring)
def door_locked():
    """
    When called, print out the strings bellow
    :param: None
    :return: None
    """
    print ""
    print "The door is locked. It's too heavy a door to break through."
    print "Continue exploring to find the key."
    print "Try looking for hidden rooms!"

def RockPaperScissors(RPSanswer):
    """
    Allows the user to play rock, paper, scissors, to simulate combat
    :param RPSanswer: str - initial user input entered to choose rock, paper, or scissors
    :return: int - 0 - the room the user is to be moved back to, win or lose
    """
    rngesus = random.randint(1,3)
    victory = False
    while victory == False:
        if answer == rngesus:
            print "You chose the same thing! You parry each others attacks, and go to fight again"
            RPSanswer = raw_input("Chose your Fight!  ")
        elif (RPSanswer == "1" and rngesus == 3) or (RPSanswer == "2" and rngesus == 1) or (RPSanswer == "3" and rngesus == 2):
            print "You strike a critical blow on the beast and slay him!"
            print "You will be taken back to the hub"
            victory = True
        elif (RPSanswer == "3" and rngesus == 1) or (RPSanswer == "1" and rngesus == 2) or (RPSanswer == "2" and rngesus == 3):
            print "The beast gets by your guard, slaying you instantly"
            print "Start again or enter done to quit"
            print "You will be taken back to the hub"
            victory = True
        return 0

def save_game():
    """
    opens and writes to the save file, overwriting the old save
    :param: None
    :return: None
    """
    save_file = open("save_file.txt", "w")
    save_file.write(str(current_room) + "\n")
    save_file.write(str(south_key) + "\n")
    save_file.write(str(north_key1) + "\n")
    save_file.write(str(north_key2) + "\n")
    save_file.close()

#reads room_file and stores it into list source_list
room_file = open("rooms.txt", "r")
source_list = room_file.readlines()
room_file.close()

#initializes empty list room_list
room_list = []

#prepare loop to fill room_list as 2d list. Loops through all lines from sourcefile.
for i in range(len(source_list)):
    #strips newline character and splits it into list of strings based on |(vertical bar)
    room_info = source_list[i].strip().split("|")
    #put string with description into room info
    description = room_info[0]
    #reads room to north, checks for none where there is no room and assigns None. Else concerts string to int and saves it to north
    if room_info[1] == "None":
        north = None
    else:
        north = int(room_info[1])
    #reads room to east, checks for none where there is no room and assigns None. Else concerts string to int and saves it to east
    if room_info[2] == "None":
        east = None
    else:
        east = int(room_info[2])
    #reads room to south, checks for none where there is no room and assigns None. Else concerts string to int and saves it to south
    if room_info[3] == "None":
        south = None
    else:
        south = int(room_info[3])
    #reads room to west, checks for none where there is no room and assigns None. Else concerts string to int and saves it to west
    if room_info[4] == "None":
        west = None
    else:
        west = int(room_info[4])
    #read room name string
    name = room_info[5]
    #create list with all correctly formatted room information
    room = [description,north,east,south,west,name]
    #append room information to roomlist
    room_list.append(room)




#main body of code, while done is not False this repeats until done is False
while done == False:
    #sets variable next_room equal to current room to prevent errors where next_room was not set in an if statement based on answer
    next_room = current_room
    #print line of whitespace (for clarity when reading) and current room's description as gotten fro mthe 2d list
    print ""
    print room_list[current_room][0]
    #get user input
    answer = raw_input("What direction do you want to go:  ")
    #changes input into all lower case
    answer = answer.lower()
    if answer == "north":
        #find out what room is indexed in the "north" spot of the current room in room_list
        next_room = room_list[current_room][1]
        #if that value is none, current room stays the same, otherwise current_ro0m becomes room indexed at north position
        if next_room == None:
            current_room = current_room
        else:
            current_room = next_room
        #various if statements for boss battles based on if the next room entered would be a boss room
        if next_room == 15:
            print "A massive cell the a large arching ceiling. Torches blaze on the wall. The entire cell has taken massive damage from the beast in there. He is massive, covered in tattoos, brand marks, and scars. He sees you and charges. You must prepare yourself to fight. "
            print "You are fighting the dungeon boss! Use rock paper scissors to simulate the fight."
            print "1 is rock, 2 is paper, and 3 is scissors."
            RPSanswer = raw_input("Chose your Fight!  ")
            current_room = RockPaperScissors(RPSanswer)
        elif next_room == 27:
            print "A massive room, at one time it may have been a ballroom or fancy dining room. All of a sudden the candles all go out, and an army of ghosts appear. They are dressed in old fashioned clothing, and as they swirl around you you feel them touching and grabbing at you. Their leader arises from the ground, and you prepare for combat"
            print "You are fighting the ghost king! Use rock paper scissors to simulate the fight."
            print "1 is rock, 2 is paper, and 3 is scissors."
            RPSanswer = raw_input("Chose your Fight!  ")
            current_room = RockPaperScissors(RPSanswer)
    elif answer == "east":
        #same as north, except checks number indexed in east instead of north
        next_room = room_list[current_room][2]
        if next_room == None:
            current_room = current_room
        else:
            current_room = next_room
        #if the next room would be 27 (only room to east of hub) runs through this chase segment instead
        if next_room == 28:
            print ""
            print "You fall out of the portal and into a dark forest. It is deathly silent."
            print "All of a sudden, a terrifying roar breakes through the silence and starts to run towards you"
            print ""
            answer = raw_input("What direction do you want to go:  ")
            print "You run as fast as you can, but the thundering hooves is gaining ground on you."
            print ""
            answer = raw_input("What direction do you want to go:  ")
            print "You can feel the monster's breath on your back."
            print ""
            answer = raw_input("What direction do you want to go:  ")
            print "You trip and fall. A massive centaur is rushing towards you. Prepare to fight!"
            print "You are fighting the dungeon boss! Use rock paper scissors to simulate the fight."
            print "1 is rock, 2 is paper, and 3 is scissors."
            RPSanswer = raw_input("Chose which of the techniques you'll use!  ")
            current_room = RockPaperScissors(RPSanswer)
        #room 18 has a key, sets the key variable to true
        elif next_room == 18:
            north_key1 = True
    elif answer == "south":
        #same as north, except checks number indexed in south instead of north
        next_room = room_list[current_room][3]
        if next_room == None:
            current_room = current_room
        else:
            current_room = next_room
        if next_room == 43:
            print "You stumble out into an open area at the heart of the maze. A wizard stand there with his cauldron, illuminating the entire area with wraithlight. He sees you, and prepares to fight you."
            print "You are fighting the ghost Wizard! Use rock paper scissors to simulate the fight."
            print "1 is rock, 2 is paper, and 3 is scissors."
            RPSanswer = raw_input("Chose which of the techniques you'll use!  ")
            current_room = RockPaperScissors(RPSanswer)
        #if the next room is 24 and they don't have the key, execute the door_locked function and set current_room back to the room they were in
        if next_room == 24 and north_key1 == False:
            door_locked()
            current_room = 22
        #set key to true
        if next_room == 24:
            north_key2 = True
    elif answer == "west":
        #same as north, except checks number indexed in west instead of north
        next_room = room_list[current_room][4]
        if next_room == None:
            current_room = current_room
        else:
            current_room = next_room
        #Execute's door_locked if not have key, go back to previous room
        if next_room == 7 and south_key == False:
            door_locked()
            current_room = 2
        elif next_room == 25 and north_key2 == False:
            door_locked()
            current_room = 16
    #three cells to north, allows user to explore all of them by entering 1, 2, or 3
    elif current_room == 3:
        if answer == "1":
            print ""
            print room_list[4][0]
            current_room = 3
        elif answer == "2":
            print ""
            print room_list[5][0]
            current_room = 3
            south_key = True
        elif answer == "3":
            print ""
            print room_list[6][0]
            current_room = 3
        #fixed bug if done or save was input while looking for room 1,2,3 would not exit/save
        elif answer == "done":
            done = True
        elif answer =="save":
            save_game()
            done = True
    #exits loop/game by setting done to true when done input
    elif answer == "done":
        done = True
    #triggers pokemon easteregg in room 8
    elif answer == "ride" and current_room == 8:
        print ""
        print " Oak's words echoed... \"There's a time and place for everything! But not now.\""
    #if user input is help, provides help advice
    elif answer == "help":
        print ""
        print "Move around the map by typing north, south, east, and west"
        print "If you keep getting lost try drawing a map on a peice of paper"
        print "The descriptions of the rooms give you hints on what to do"
        print "When you're done, type done to exit"
        print "Type save to save and quit"
    #executes save function if save input
    elif answer =="save":
        save_game()
        done = True
    #otherwise input not recognized, try again
    else:
        print ""
        print "Your input was not recognized"
    #if next_room is none, tell themn you can't go this way
    if next_room == None:
        print ""
        print "You cannot go this way"




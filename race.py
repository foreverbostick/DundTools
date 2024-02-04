#
# Player selectable races for D&D character creation
#

finalPick = ''
# Add selectable races to an array
races = ["Dragonborn", "Hill Dwarf", "Mountain Dwarf", "High Elf", "Wood Elf", "Rock Gnome", "Deep Gnome", "Half Elf", "Half Orc", "Lightfoot Halfling", "Stout Halfling", "Human", "Variant Human","Tiefling"]
stats = ["Str", "Dex", "Con", "Int", "Wis", "Cha"]

#
# Function to take user selection
#
# Basically the main block of the module
#
def chooseRace():
    global raceChoice
    global raceIndex
    global r8
    global finalPick

    print("Choose from the following races (enter the number):\n")
    # Print out the races in a numbered list
    for i in enumerate(races):
        print(i[0]+1,') ', i[1])
    raceChoice = input("\n--> ")
    print('\n')
    
    # Take the input and use it to choose from the list of races
    raceIndex = int(raceChoice) - 1
    finalPick = raceList[raceIndex]
    # Convert raceChoice to a string
    raceChoice = races[int(raceChoice) - 1]

    # If statements for races with player-selectable stat mods
    if raceChoice == "Half Elf":
        hePlus()
    if raceChoice == "Variant Human":
        vhPlus()

    
# Create a class for races and their different stat mods
class Race:
    
    def __init__(self, strAdd, dexAdd, conAdd, intAdd, wisAdd, chaAdd):
        self.strAdd = strAdd
        self.dexAdd = dexAdd
        self.conAdd = conAdd
        self.intAdd = intAdd
        self.wisAdd = wisAdd
        self.chaAdd = chaAdd

    def show(self):
        if raceChoice != "":
            print("Race:", raceChoice, "\nStr:", self.strAdd, "\nDex:", self.dexAdd,
                "\nCon:", self.conAdd, "\nInt:", self.intAdd,
                "\nWis:", self.wisAdd, "\nCha:", self.chaAdd,"\n")



# Variables for races with their various stat mods
r1 = Race(2, 0, 0, 0, 0, 1)
r2 = Race(0, 0, 0, 0, 1, 0)
r3 = Race(2, 0, 0, 0, 0, 0)
r4 = Race(0, 0, 0, 1, 0, 0)
r5 = Race(0, 0, 0, 0, 1, 0)
r6 = Race(0, 0, 1, 0, 0, 0)
r7 = Race(0, 1, 0, 0, 0, 0)
r8 = Race(0, 0, 0, 0, 0, 2)
r9 = Race(2, 0, 1, 0, 0, 0)
r10 = Race(0, 0, 0, 0, 0, 1)
r11 = Race(0, 0, 1, 0, 0, 0)
r12 = Race(1, 1, 1, 1, 1, 1)
r13 = Race(0, 0, 0, 0, 0, 0)
r14 = Race(0, 0, 0, 1, 0, 2)

# Set up a list of all the race variables to choose from later
raceList = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14]

#
# Half elves get a +1 to a stat of the player's choice,
# so we need a function to get that choice
#
def hePlus():
    global plusChoice1
    global heNewStats
    global r8
    global finalPick
    heStats = [r8.strAdd, r8.dexAdd, r8.conAdd, r8.intAdd, r8.wisAdd, r8.chaAdd]
    
    # List stats to choose from
    print('Choose a stat to add +1 to (enter the number)')
    for i in enumerate(stats[:5]):
        print(i[0]+1,') ', i[1])
    plusChoice1 = input('\n--> ')
    print('\n')

    index = plusChoice1
    # Convert plusChoice1 to string
    plusChoice1 = stats[int(plusChoice1) - 1]
    # Set chosen stat to 1
    heStats[int(index) - 1] = 1
    
    # Get updated values for class instance and pass them back globally
    r8 = Race(heStats[0], heStats[1], heStats[2], heStats[3], heStats[4], heStats[5])
    finalPick = r8
    return r8, finalPick


#
# Variant humans get a +1 to two different stats, so we need
# a second function for those choices
#
def vhPlus():
    global plusChoice1
    global plusChoice2
    global r13
    global finalPick
    vhStats = [r13.strAdd, r13.dexAdd, r13.conAdd, r13.intAdd, r13.wisAdd, r13.chaAdd]

    print('Choose a stat to add +1 to (enter the number)')
    for i in enumerate(stats):
        print(i[0]+1,') ', i[1])
    plusChoice1 = input('\n--> ')
    print('\n')

    index = plusChoice1
    plusChoice1 = stats[int(plusChoice1) - 1]
    vhStats[int(index) - 1] = 1

    # Do it all over again
    print('Choose another stat to add +1 to (enter the number)')
    for i in enumerate(stats):
        print(i[0]+1,') ', i[1])
    plusChoice2 = input('\n--> ')
    print('\n')

    index = plusChoice2
    plusChoice2 = stats[int(plusChoice2) - 1]
    vhStats[int(index) - 1] = 1

    r13 = Race(vhStats[0], vhStats[1], vhStats[2], vhStats[3], vhStats[4], vhStats[5])
    finalPick = r13
    return r13, finalPick

if __name__ == "__main__":
    chooseRace()

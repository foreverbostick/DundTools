#
# Player character stat modifiers
#

# Import race stat mods
from race import * as r

# Check to see if race selection has been made, and if not, print a message
def raceCheck():
    if r.finalPick == '' or False:
        gotoRace = input('You need to select a race first. Run the race module now? y/n\n--> ')
        while True:
            if gotoRace.lower == 'yes' or 'y':
                r.chooseRace()
            else:
                print('Goodbye!')
                break

class Mods:

    def __init__(self, strMod, dexMod, conMod, intMod, wisMod, chaMod):
        self.strMod = strMod
        self.dexMod = dexMod
        self.conMod = conMod
        self.intMod = intMod
        self.wisMod = wisMod
        self.chaMod = chaMod

    def show(self):
        print('Str:', self.strMod, '\nDex:', self.dexMod,
              '\nCon:', self.conMod, '\nInt:', self.intMod,
              '\nWis:', self.wisMod, '\nCha:', self.chaMod, '\n')

stats = Mods(0, 0, 0, 0, 0, 0)

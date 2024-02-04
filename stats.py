#
# Player character stat modifiers
#

# Import race stat mods
import race as r


# Check to see if race selection has been made, and if not, print a message
def raceCheck():
    if r.finalPick == '' or False:
        gotoRace = input('You need to select a race first. Run the race module now? y/n\n--> ')
        while True:
            if gotoRace.lower == 'yes' or 'y':
                r.chooseRace()
                break
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

statMods = Mods(0, 0, 0, 0, 0, 0)

def addMods():
    global statMods
    statMods = Mods(statMods.strMod + r.finalPick.strAdd,
                    statMods.dexMod + r.finalPick.dexAdd,
                    statMods.conMod + r.finalPick.conAdd,
                    statMods.intMod + r.finalPick.intAdd,
                    statMods.wisMod + r.finalPick.wisAdd,
                    statMods.chaMod + r.finalPick.chaAdd)

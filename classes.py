#
# D&D player character classes
#

import stats as s
import race as r

className = ''
strSave = 0
dexSave = 0
conSave = 0
intSave = 0
wisSave = 0
chaSave = 0

saves = [0 0 0 0 0 0]

class Class:
    def __init__(self, className, strSave, dexSave, conSave,
                 intSave, wisSave, chaSave):
        self.className = className
        self.strSave = strSave
        self.dexSave = dexSave
        self.conSave = conSave
        self.intSave = intSave
        self.wisSave = wisSave
        self.chaSave = chaSave

    def show(self):
        print("Class:", self.className,)


def pushSaves():
    global saves


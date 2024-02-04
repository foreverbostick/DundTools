# A simple program to roll 3d6, to randomly generate stats
# for DnD character creation
#
# Rolls 3d6 3 times and returns the largest resulting roll
#
# In my experience, rolling the set 3x reduces the number of
# low rolls. It's still completely random and possible to roll
# less than 8, but doing it this way makes it somewhat less likely

from random import randint

def statRoll():
    rolls = []
    for i in range(3):
        rollResult = randint(3, 18)
        rolls.append(rollResult)
    
    max = rolls[0]
    for x in rolls:
        if x > max:
            max = x

    return max

statRoll()

from random import randint
import sys

# Take the command line argument for what the user wants to roll
rollChoice = str(sys.argv[1])

# Help argument
if rollChoice == 'help' or '':
    print("\nEnter the amount of dice you'd like to roll, the letter 'd', the number of sides of the die, and +/- a number to add a modifier.\n\nEx: 3d6+5")
    sys.exit()
else:
    print('You entered: ' + rollChoice)

# Find the 'd' in the input
dIndex = rollChoice.find('d')
if dIndex == -1:
    raise Exception('Missing the "d" character. Enter "diceroll help" for instructions.')

# Find the number of dice to roll
diceNum = rollChoice[:dIndex]
if not diceNum.isdecimal():
    raise Exception('Missing the number of dice. Enter "diceroll help" for instructions.')
diceNum = int(diceNum)

# See if there's a modifier to add/subtract
modIndex = rollChoice.find('+')
if modIndex == -1:
    modIndex = rollChoice.find('-')

# Find the type of dice to roll
if modIndex == -1:
    diceType = rollChoice[dIndex + 1 :]
else:
    diceType = rollChoice[dIndex + 1 : modIndex]
if not diceType.isdecimal():
    raise Exception('Missing type of dice. Enter "diceroll help" for instructions.')
diceType = int(diceType)

if modIndex == -1:
    diceMod = 0
else:
    diceMod = int(rollChoice[modIndex + 1 :])
    if rollChoice[modIndex] == '-':
        # Switch to negative to subtract
        diceMod = -diceMod

# Do the math
rolls = []
for i in range(diceNum):
    rollResult = randint(1, diceType)
    rolls.append(rollResult)

# Display the total
print('\nTotal: ', sum(rolls) + diceMod, '\n(Each die: ', end='')

# Show individual rolls
for i, roll in enumerate(rolls):
    rolls[i] = str(roll)
print(', '.join(rolls), end='')

# Display mod amount
if diceMod != 0:
    modSign = rollChoice[modIndex]
    print(', {}{}'.format(modSign, abs(diceMod)), end='')
print(')')

# Call out natural 20s and 1s
if rolls[i] == '20' and diceType == 20:
    print('\nNat 20!')
if rolls[i] == '1' and diceType == 20:
    print('\nOh no! Nat 1 :(')

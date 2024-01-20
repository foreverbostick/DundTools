from random import randint
import sys, math

# Make a little title bar thing
print('''
            -=-=-=-=-=-=-=-=-=-=-=-
            DundTools DiceRoll v0.1
            -=-=-=-=-=-=-=-=-=-=-=-
Dungeons & Dragons (or general, really) Dice Roller

        More info is available on Github

    https://github.com/foreverbostick/DundTools

  Type 'QUIT' at any time to close the application
''')

while True:                     # Main loop
    try:
        
        # Gather all the information we need from the user
        diceType = input('What kind of dice are you wanting to roll?\n\n> ')
        if diceType.upper() == 'QUIT':
            print('\nThanks for playing!\n')
            sys.exit()

        diceNum = input('How many dice do you want to roll?\n\n> ')
        if diceNum.upper() == 'QUIT':
            print('\nThanks for playing!\n')
            sys.exit()
        
        diceMod = input('Any modifiers?\n(Ex - +5 or -1. Leave blank for 0)\n\n> ')

        if diceMod == '' or '+0' or '-0':
            diceMod = '+0'
        if diceMod.upper() == 'QUIT':
            print('\nThanks for playing!\n')
            sys.exit()
        
        # Combine all the inputs into a single string
        diceRoll = diceNum + 'd' + diceType + diceMod

        # Find the d and +/- in the string, to make organizing easier
        dIndex = diceRoll.find('d')
        modIndex = diceRoll.find('+')
        if modIndex == -1:
            modIndex = diceRoll.find('-')

        # Do the actual math
        rolls = []
        for i in range(diceNum):
            rollResult = randint(1, diceType)
            rolls.append(rollResult)

        diceConfirm = input('\nYou said you wanted to roll ' + diceNum + 'd' + diceType + diceMod + '. Does this look correct? (Y/N)\n\n> ')
        if diceConfirm.upper() == 'QUIT':
            print('\nThanks for playing!\n')
            sys.exit()
        # I'm sure there's a better way to get confirmation,
        # but this works as a placeholder

        # Convert diceNum and diceMod string to int so we can do math
        diceNum = diceRoll[:dIndex]
        diceNum = int(diceNum)
        diceMod = diceRoll[modIndex:]
        diceMod = int(diceMod)

        # Show the total
        print('Total: ', sum(rolls) + diceMod, '(Each Die: ', end='')

        # Show the individual rolls
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        # Display the modifier amount
        if diceMod != 0:
            modSign = diceRoll[modIndex]
            print(', {}{}'.format(modSign, abs(diceMod)), end='')
        print(')')

    except Exception as exc:
        print('Error! Here\'s what happened: ' + str(exc))
        continue

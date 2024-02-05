from random import randint
import sys

rollChoice = str(sys.argv[1])

def rollDice():
    if rollChoice == 'help' or '':
        invalidInput()
        sys.exit()
    else:
        print('You entered: ' + rollChoice)

    dIndex = rollChoice.find('d')
    if dIndex == -1:
        invalidInput()

    diceNum = rollChoice[:dIndex]
    if not diceNum.isdecimal():
        invalidInput()
    diceNum = int(diceNum)

    modIndex = rollChoice.find('+')
    if modIndex == -1:
        modIndex = rollChoice.find('-')

    if modIndex == -1:
        diceType = rollChoice[dIndex + 1 :]
    else:
        diceType = rollChoice[dIndex + 1 : modIndex]
    if not diceType.isdecimal():
        invalidInput()
    diceType = int(diceType)

    if modIndex == -1:
        diceMod = 0
    else:
        diceMod = int(rollChoice[modIndex + 1 :])
        if rollChoice[modIndex] == '-':
            diceMod = -diceMod

    rolls = []
    for i in range(diceNum):
        rollResult = randint(1, diceType)
        rolls.append(rollResult)

    print('\nTotal:', sum(rolls) + diceMod, '\n(Each die:', end='')

    for i, roll in enumerate(rolls):
        rolls[i] = str(roll)
    print(', '.join(rolls), end='')

    if diceMod != 0:
        modSign = rollChoice[modIndex]
        print(', {}{}'.format(modSign, abs(diceMod)), end='')
    print(')')

    if rolls[i] == '20' and diceType == 20:
        print('\nNat 20!')
    if rolls[i] == '1' and diceType == 20:
        print('\nOh no! Nat 1 :(')

if __name__ == '__main__':
    rollDice()

def invalidInput():
    raise Exception('Invalid argument. Use the following format:\n\n3d6+4\n1d20\n10d4-7\n')

import re
import random

with open('dictionary.txt') as dictInput:
    dictionary = dictInput.readlines()


wordLength = input('Please enter a word length. ')
while not re.match('^[0-9]*$', wordLength):
    wordLength = input('Please enter a number. ')


lenCheck = False
for word in dictionary:
    if len(word) == int(wordLength):
        lenCheck = True

while not lenCheck:
    wordLength = input('There are no words of that length in the dictionary. ')
    for word in dictionary:
        if len(word) == int(wordLength):
            lenCheck = True


numGuess = input('Please enter the maximum number of guesses. ')
while not re.match('^[0-9]*$', numGuess):
    numGuess = input("Please enter a number. ")

remaining = input('Would you like to see the size of the current dictionary? Enter Y or N. ')
while not re.match('^(Y|N){1}$', remaining.upper()):
    remaining = input('Please enter Y or N. ')
blankBank = '_ ' * int(wordLength)
pastGuesses = {}
numGuess = int(numGuess)
families = {}
for word in dictionary:
    if len(word ) -1 == int(wordLength):
        families.update({word: ''})
prevGuesses = []
wordState = []
stillPlaying = True
for i in range(int(wordLength)):
    wordState.append('-')
while numGuess > 0:
    finalWord = str(families)
    if len(families) == 1:
        print('You won! The word was ' + finalWord)
        break
    wordOutput = (' '.join(wordState))
    if remaining == 'Y':
        userGuess = input(wordOutput + 'You have ' + str(numGuess) + ' guesses left. There are ' + str
            (len(families)) + ' entries left in the dictionary. You have already guessed ' + str(prevGuesses) + '. Please enter your next guess. /n Blank Word: ' + ('_  '* int(wordLength)))
    else:
        userGuess = input(wordOutput + 'You have ' + str(numGuess) + ' guesses left. There are ' + str
            (len(families)) + ' entries left in the dictionary. You have already guessed ' + str(prevGuesses) + '. Please enter your next guess. /n Blank Word: ' + ('_ '* int(wordLength)))
    while not ( re.match('^[a-z]{1}$', userGuess) and not (userGuess in prevGuesses)):
        userGuess = input("Please enter a single letter that has not been guessed. ")
    


    prevGuesses.append(userGuess)

    removeList = []

    optFam = {}
    for word, key in list(families.items()):
        currentKey = userGuess
        try:
            prevKey = families.get(word)
        except:
            pass

        indexCount = 0
        word.strip()
        for letter in word:
            if letter == userGuess:
                currentKey = currentKey +', ' + str(indexCount)
            indexCount = indexCount + 1

        if currentKey != userGuess:
            if not prevKey:
                families.update({word: currentKey})
            else:
                families.update({word: prevKey + ', ' + currentKey})
        if not families[word] in optFam:
            optFam[families[word]] = 0
        elif families[word] in optFam:
            optFam[families[word]] = optFam[families[word]] + 1

        currentOptCount = 0
        for nums in list(optFam.values()):
            if nums > currentOptCount:
                currentOptCount = nums

        keyList = list(optFam.keys())
        valList = list(optFam.values())
        ind = valList.index(currentOptCount)
        optKey = keyList[ind]
        if families.get(word) != optKey:
            removeList.append(word)

    for word in removeList:
        if word in families:
            families.pop(word)
    numGuess = numGuess - 1

    if len(optKey) > 0:
        tempKey = optKey.split(',')
        wordState[int(tempKey[1])] = tempKey[0]

    if numGuess == 0 and len(families) > 1:
        print('You lost!')
    if numGuess == 0 and len(families) == 1:
        print('You won! The word was ' + str(families))

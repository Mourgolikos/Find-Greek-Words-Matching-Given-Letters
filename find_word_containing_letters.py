# -*- coding: utf-8 -*-
__author__ = 'Triantafyllos Paschaleris'


import collections
import pprint


##### VALUES TO BE CHANGED
wantedLetters = "ΚΛΕΡΙΑΤΑΟΠΤ"#order doesn't matter
howManyLettersWanted = 8#the total number of letter the hidden word consists of

fixedLetters = {
#letter:position
    "Ε":6,
    "Α":8
}
##### END OF CHANGEABLE VALUES


howManyLetterToSearchFor = howManyLettersWanted- len(fixedLetters)


matchedWordsList = {}

with open("searchReadyWordsOfLength"+str(howManyLettersWanted)+".txt","r",encoding='utf-8') as f:
    wordsList = f.readlines()


for word in wordsList:
    for fixedLetter,position in  fixedLetters.items():
        if not word[position-1]==fixedLetter:
            break
    else:#all the fixed letters have been so the loop ended normally.
        #so let's search for the other letters

        matchingCounter = 0

        tempWantedLetters = wantedLetters

        for letter in word:
            if letter in tempWantedLetters:
                matchingCounter += 1
                tempWantedLetters = tempWantedLetters.replace(letter,"",1)
            else:
                break
        if matchingCounter >= howManyLetterToSearchFor:
            matchedWordsList.setdefault(matchingCounter, []).append(word.replace("\n",""))#append the words in the dict and remove the newline character (for prettier prints)

matchedWordsList = collections.OrderedDict(sorted(matchedWordsList.items(),reverse=True))#sort the dict be desc order
pprint.pprint(matchedWordsList)

with open("matchedWordsOfLength" + str(howManyLettersWanted) + ".txt",'w', encoding='utf-8') as f:
    pprint.pprint(matchedWordsList,f)
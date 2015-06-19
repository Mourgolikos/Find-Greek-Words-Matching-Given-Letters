# -*- coding: utf-8 -*-
__author__ = 'Triantafyllos Paschaleris'


import collections
import pprint


##### VALUES TO BE CHANGED
wantedLetters = "ΘΡΞΕΣΡΑΖΦΟΠΩΗΜΑ"#order doesn't matter
howManyLettersWanted = 11#the total number of letter the hidden word consists of

fixedLetters = {
#position:letter
    1:"Π",
    3:"Ρ",
}
##### END OF CHANGEABLE VALUES


howManyLetterToSearchFor = howManyLettersWanted - len(fixedLetters)


matchedWordsList = {}

with open("searchReadyWordsOfLength"+str(howManyLettersWanted)+".txt","r",encoding='utf-8') as f:
    wordsList = f.readlines()


for word in wordsList:
    word = word.replace("\n","")#words have a newline character as read from the file, so it has to be removed
    for position,fixedLetter in  fixedLetters.items():
        if not word[position-1]==fixedLetter:
            break
    else:#all the fixed letters have been found so the loop ended normally.
        #so let's search for the other letters

        matchingCounter = 0

        tempWantedLetters = wantedLetters#set a temp variable in order to be used the the .replace method below

        for letter in word:
            if letter in tempWantedLetters:
                matchingCounter += 1
                tempWantedLetters = tempWantedLetters.replace(letter,"",1)#removing the found letter for the wanted letters, and continue searching for the rest letters
            else:
                break
        else:#all the letters matched the wanted letters set and the loop finished normally
            if matchingCounter >= howManyLetterToSearchFor:
                matchedWordsList.setdefault(matchingCounter, []).append(word)#append the words in the dict

matchedWordsList = collections.OrderedDict(sorted(matchedWordsList.items(),reverse=True))#sort the dictionary by descending order
pprint.pprint(matchedWordsList)

#outputFilename = "matchedWordsOfLength" + str(howManyLettersWanted) + ".txt"
#print("Script Finished! Check the file: " + outputFilename)
#with open(outputFilename,'w', encoding='utf-8') as f:
#    pprint.pprint(matchedWordsList,f)
# -*- coding: utf-8 -*-
__author__ = 'Triantafyllos Paschaleris'



import pprint



##### VALUES TO BE CHANGED
givenLetter = "ΑΒΓΟ"
##### END OF CHANGEABLE VALUES


matchedWordsList = []


fileName = "searchReadyWordsOfLength" + str(len(givenLetter)) + ".txt"
with open(fileName,"r",encoding='utf-8') as f:
    wordsList = f.readlines()


for word in wordsList:
    word = word.replace("\n","")#words have a newline character as read from the file, so it has to be removed
    tempGivenLetters = givenLetter
    for letter in word:
        if letter in tempGivenLetters:
            tempGivenLetters = tempGivenLetters.replace(letter,"",1)#removing the found letter for the wanted letters, and continue searching for the rest letters
        else:
            break
    else:
         matchedWordsList.append(word)#append the words in the list


pprint.pprint(matchedWordsList)
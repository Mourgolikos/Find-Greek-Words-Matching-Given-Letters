# -*- coding: utf-8 -*-
__author__ = 'Triantafyllos Paschaleris'



import collections
import pprint



alphabet = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"


##### VALUES TO BE CHANGED
wordLength = 10

fixedLetters = {
#position:letter
    1:"Π",#First Given Letter.
    wordLength:"Ρ",#Last Given Letter.
}
##### END OF CHANGEABLE VALUES


matchedWordsList = []
lettersFrequency = {}


fileName = "searchReadyWordsOfLength" + str(wordLength) + ".txt"
with open(fileName,"r",encoding='utf-8') as f:
    wordsList = f.readlines()


for word in wordsList:
    word = word.replace("\n","")#words have a newline character as read from the file, so it has to be removed
    for position,fixedLetter in  fixedLetters.items():
        if not word[position-1]==fixedLetter:
            break
    else:
        if word[0]==fixedLetters[1]:
            if fixedLetters[wordLength] == "" or word[-1] == fixedLetters[wordLength]:
                matchedWordsList.append(word)#append the words in the list
                for letter in word[1:-1]:#Counting the frequency of the letters in the word, apart from the given first and last letters
                    lettersFrequency[letter] = lettersFrequency.setdefault(letter, 0) + 1#increase by one the counter of the letter (if it doesn't exist just get a default value of zero)


pprint.pprint(matchedWordsList)
lettersFrequency = collections.OrderedDict(sorted(lettersFrequency.items(), key=lambda t: t[1],reverse=True))#sort the dictionary by values in descending order
pprint.pprint(lettersFrequency)
__author__ = 'Triantafyllos Paschaleris'


punctuation = {#In order to remove the Greek punctuation
    u"ά" :   u"α",
    u"Ά" :   u"α",
    u"ό" :   u"ο",
    u"Ό" :   u"Ο",
    u"έ" :   u"ε",
    u"Έ" :   u"ε",
    u"ί" :   u"ι",
    u"Ί" :   u"ι",
    u"ή" :   u"η",
    u"Ή" :   u"η",
    u"ώ" :   u"ω",
    u"Ώ" :   u"ω",
    u"ύ" :   u"υ",
    u"Ύ" :   u"υ",
    u"ϊ" :   u"ι",
    u"ϋ" :   u"υ",
    u"ΐ" :   u"ι",
    u"ΰ" :   u"υ",
}


outputFilePrefix = "searchReadyWordsOfLength"
outputFileExtension = ".txt"


minWordLength = 1
newWordLists = {}

with open("greek_words.txt","r",encoding="utf-8") as f:#read all the greek words from the dictionary provided and prepare them
    words = f.readlines()
    print("Reading and converting the words")
    for word in words:
        if len(word)>minWordLength+1:#get the words of min length
            length=len(word)
            newWord = ""#reset the word buffer
            for letter in word:
                if letter.isalpha():#check if character is an alphabet's letter in order to avoid error
                    newWord += punctuation.get(str(letter),str(letter))
            newWordLists.setdefault(length-1, []).append(newWord.upper()+"\n")#append the new capitalized and non-punctuated word in the new list in order to be written to file later

for length in newWordLists.keys():#let's write the words in files according to their lengths (sizes)
    filename = outputFilePrefix+str(length)+outputFileExtension
    with open(filename,'w',encoding="utf-8") as f:
        print("Now writing the new Word List in the file: " + filename)
        f.writelines(newWordLists[length])

print("All is done!")
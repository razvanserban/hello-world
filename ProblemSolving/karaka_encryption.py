"""
Make a function that encrypts a given input with these steps:
Input: "apple"
Step 1: Reverse the input: "elppa"
Step 2: Replace all vowels using the following chart:
a => 0
e => 1
i => 2
o => 2
u => 3
# "1lpp0"
Step 3: Add "aca" to the end of the word: "1lpp0aca"
Output: "1lpp0aca"
"""
def reverseWord(word):
    #reverse given word
    newWord = ''
    for character in word:
        newWord = str(character) + newWord
    return(newWord)

def replaceCharacter(word):
    #replace characters in a word
    newWord = ''
    translateDictionary = {'a':'0','e':'1','i':'2','o':'2','u':'3'}
    for character in word:
        if character in translateDictionary.keys():
            character = translateDictionary[character]
        newWord += character
    return(newWord)

def appendCharacters(word):
    #append string to word
    newWord = ''
    newWord = word + 'aca'
    return(newWord)

print(appendCharacters(replaceCharacter(reverseWord('Popocatepetl'))))
import re

def translateWordToPigLatin(word):
    isWordCapitalized = word[0].isupper()

    word = word.lower()

    if word[0] == 'y':
        firstConsonants = re.findall("^[^aeiou]+", word, re.IGNORECASE)
        firstConsonants = firstConsonants[0] if firstConsonants else ""
        
        restOfTheString = re.findall("[aeiou].*", word, re.IGNORECASE)
        restOfTheString = restOfTheString[0] if restOfTheString else ""

    else:
        firstConsonants = re.findall("^[^aeiouy]+", word, re.IGNORECASE)
        firstConsonants = firstConsonants[0] if firstConsonants else ""
        
        restOfTheString = re.findall("[aeiouy].*", word, re.IGNORECASE)
        restOfTheString = restOfTheString[0] if restOfTheString else ""
    
    translatedWord = restOfTheString + firstConsonants + "ay"

    if isWordCapitalized:
        translatedWord = translatedWord[0].upper() + translatedWord[1:]

    return translatedWord


def translateStringToPigLatin(string):
    words = string.split()

    translatedString = ""

    for word in words:
        punctuation = re.findall("[^A-Za-z0-9]+", word)
        word = re.sub("[^A-Za-z0-9]+", "", word)

        begPunctuation = ""
        endPunctuation = ""
        if len(punctuation) > 1:
            begPunctuation = punctuation[0]
            endPunctuation = punctuation[-1]
        elif punctuation:
            endPunctuation = punctuation[0]

        if(word):
            translatedWord = translateWordToPigLatin(word)

        translatedString += begPunctuation + translatedWord + endPunctuation + " "

    return translatedString
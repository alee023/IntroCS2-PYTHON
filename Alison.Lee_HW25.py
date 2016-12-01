"""
TEAM RAD -- Ryan Siu, Alison Lee, David Cheung
IntroCS2 pd8
HW25 -- Improvements, Improvements...
2016-04-01


PIG LATIN RULES:
1. If first two are consonants, then move both first two to the end and add -ay
2. If first letters are consonant and vowel, then move first letter to the end and add -ay
3. If first is vowel, then add -way


OUTLINE:

7 functions
        1. Vowel checking function
        2. Word translation function
            - Conditional in the main function that separates into 3 other functions
        3. Phrase translation function
            - Uses the word translation function to translate phrases
        4. Upper/lowercase checking function
        5. isLetter checking function
        6. Punctuation function
            - Returns the punctuation that a word contains
        7. Punctuation removing function
            - Returns a phrase without punctuation


DEVELOPMENT PLAN:

    1. Write a function that checks whether a letter is a vowel or not
    2. Write a word function that separates words into the different categories of the rules
    3. Write a phrase function that uses the word translation function to translate phrases
    4. Add checks for special cases to make our code foolproof (check below)


THINGS WE HAVE TO TAKE INTO ACCOUNT:
- Upper/lowercase
- Punctuation
- If length of word is 1, then don't check the second character


DEVELOPMENT LOG:

v1.0 changes
 - 2016-03-29 8:10 PM
   RS, AL, DC: Finished RULES, OUTLINE, DEVELOPMENT PLAN
 - 2016-03-29 8:18 PM
   RS: Finished and tested isVowel(ch) function
 - 2016-03-29 8:36 PM
   AL: Added check for if length of word is 1 to THINGS WE HAVE TO TAKE INTO ACCOUNT
 - 2016-03-29 8:40 PM
   RS, AL, DC: Finished and tested wordTranslate(word) function
 - 2016-03-30 2:00 PM
   RS, AL, DC: Finished and tested isUpper(letter), isLetter(ch), worked on
               translate(phrase)
 - 2016-03-30 7:05 PM
   RS, AL, DC: Finished and tested punctuation functions, translate(phrase)
   
v1.1 changes
 - 2016-04-01 1:30 PM
   RS: Changed the isVowel and isLetter functions to use the .find() method
   Credit to Team #wewantlists

"""


# Takes a character as an input, returns True if ch is a vowel, False if it's not
def isVowel(ch):

    # Changes ch to lowercase so that uppercase doesn't also need to be checked
    ch = ch.lower()
    
    # List of vowels in a string
    vowels = "aeiou"
    
    return vowels.find(ch) != -1


# Takes a word as an input, returns any punctuation that a word contains at the end
def punctuation(word):
    index = 0

    # Loops through the word until punctuation is found or until the end of the word,
    # pesky apostrophes are removed and not included in the final translation
    while index < len(word) and (isLetter(word[index]) or word[index] == "'"):
        index += 1

    # Return only the end of the string, where the punctuation is
    return word[index:]


# Takes a word as an input, returns the Pig Latin translation of a word
def wordTranslate( word ) :

    # Uses isVowel to check for the first (and second) letter
    first = word[ 0 ]
    
    # Sets whether or not the first letter is capitalized to caps
    caps = isUpper(first)
    
    # Lowers the first letter to normalize the letter when it's moved
    first = first.lower()
    
    # If the length of the word is more than 1, a second local variable called 
    # second is created. It stores the second letter of the word
    if len( word ) > 1 : 
        second = word[ 1 ]
        
    # Stores the punctuation in punc, and removes the punctuation from word for
    # easier formatting; we'll add any punctuation in later
    punc = punctuation(word)
    word = removePunctuation(word)
        
    # If the first letter is a vowel, "way" is added to the end of the word. (Rule #3)
    if isVowel(first) == True:
        word = word + "way" + punc
        
    # At this point, the first letter of the word should be a consonant and this
    # tests for the second letter. If it is a consonant as well, it will move
    # both the first and second letter to the end of the word and add "ay" (Rule #2)
    elif isVowel(second) == False:
        word = word[ 2 : ] + first + second + "ay" + punc
        
    # Tests for the second letter of the word. The first should be a consonant.
    # If it is true, move only the first to the end + add "ay" (Rule #1)
    else :
        word = word[ 1 : ] + first + "ay" + punc

    # If the first letter was capitalized, then recapitalize the new first letter
    if caps:
        return word.capitalize()
    
    return word


# Takes a character as an input, returns whether or not character is a letter
def isLetter(ch):

    # Takes uppercase letters into consideration
    ch = ch.lower()

    # List of letters in a string, list of uppercase letters are also added
    letters = "abcdefghijklmnopqrstuvwxyz"
    
    return letters.find(ch) != -1

    
# Takes a letter as an input, returns whether or not the letter is capitalized
def isUpper( letter ) :
    return letter.upper() == letter


# Takes a phrase as an input, returns the phrase without punctuation
def removePunctuation(phrase):
    index = 0
    newPhrase = ""
    
    # Loops through a phrase and "removes" it by not including it in the string 
    # that is returned
    while index < len(phrase):
        if isLetter(phrase[index]):
            newPhrase += phrase[index]
        index += 1
    return newPhrase

# Takes a phrase as an input, returns a translated Pig Latin phrase
def translate(phrase):
    string = ""
    space = phrase.find(' ')
    
    # Loops through the phrase, finds each word, translates it, and concatenates
    # it with the other words to make the translated phrase
    while space != -1:
        string += wordTranslate(phrase[:space]) + ' '
        phrase = phrase[space+1:]
        space = phrase.find(' ')

    # To add the last word, which is left out in the while loop
    string += wordTranslate(phrase)
        
    return string

# Test cases
print translate("Hey there, I am Bob") # "Eyhay erethay, Iway amway Obbay"
print translate("What are the rules of Pig Latin?") # "Atwhay areway ethay ulesray ofway Igpay Atinlay?"
print translate("the pope rocks red kicks") # "ethay opepay ocksray edray ickskay"
print translate("Why... I don't feel like doing this!!!") # "Ywhay... Iway ontday eelfay ikelay oingday isthay!!!"

"""
TEAM RAD -- Ryan Siu, Alison Lee, David Cheung
IntroCS2 pd8
HW23 -- Anslatingtray Englishway intoway Igpay Atinlay
2016-03-29


PIG LATIN RULES:
1. If first two are consonants, then move both first two to the end and add -ay
2. If first letters are consonant and vowel, then move first letter to the end and add -ay
3. If first is vowel, then add -way


OUTLINE:

5 functions
***     1. Vowel checking function
***     2. Word translation function
***         - Conditional in the main function that separates into 3 other functions
        3. Phrase translation function
            - Uses the word translation function to translate phrases
        4. Upper/lowercase checking function
        5. isLetter checking function


DEVELOPMENT PLAN:

*** indicates completed

*** 1. Write a function that checks whether a letter is a vowel or not
*** 2. Write a word function that separates words into the different categories of the rules
    3. Write a phrase function that uses the word translation function to translate phrases
    4. Add checks for special cases to make our code foolproof (check below)


THINGS WE HAVE TO TAKE INTO ACCOUNT:
- Upper/lowercase
- Punctuation
- If length of word is 1, then don't check the second character
- Legit word check? (make sure word is made up of only letters)


DEVELOPMENT LOG:

 - 2016-03-29 8:10 PM
   RS, AL, DC: Finished RULES, OUTLINE, DEVELOPMENT PLAN
 - 2016-03-29 8:18 PM
   RS: Finished and tested isVowel(ch) function
 - 2016-03-29 8:36 PM
   AL: Added check for if length of word is 1 to THINGS WE HAVE TO TAKE INTO ACCOUNT
 - 2016-03-29 8:40 PM
   RS, AL, DC: Finished and tested wordTranslate(word) function
 - 2016-03-29 8:58 PM
   RS: Added legit word check to THINGS WE HAVE TO TAKE INTO ACCOUNT

"""


# Returns True if ch is a vowel, False if it's not
def isVowel(ch):

    # Changes ch to lowercase so that uppercase doesn't also need to be checked
    ch = ch.lower()
    
    return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'


# Returns the Pig Latin translation of a word
def wordTranslate( word ) :

    # Uses isVowel to check for the first (and second) letter
    first = word[ 0 ]
    
    # If the length of the word is more than 1, a second local variable called 
    # second is created. It stores the second letter of the word
    if len( word ) > 1 : 
        second = word[ 1 ]
        
    # If the first letter is a vowel, "way" is added to the end of the word. (Rule 3)
    if isVowel( first ) == True : 
        return word + "way"
        
    # At this point, the first letter of the word should be a consonant and this
    # tests for the second letter. If it is a consonant as well, it will move
    # both the first and second letter to the end of the word and add "ay" (Rule 2)
    elif isVowel( second ) == False :
        return word[ 2 : ] + first + second + "ay" 
        
    # Tests for the second letter of the word. The first should be a consonant.
    # If it is true, move only the first to the end + add "ay" (Rule 1)
    elif isVowel( second ) == True :
        return word[ 1 : ] + first + "ay"
        
    # Should never reach this point with any word. Returns debugging message 
    # if it does reach this point.
    else:
        return "\n" + "Error \n" + "first: " + first + "\n" + "second: " + second + "\n"
        
print wordTranslate("cap")
# should print "apcay"
print wordTranslate("a")
# should print "away"
print wordTranslate("chopper")
# should print "opperchay"
    

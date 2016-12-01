# Team Green - Erick Cho & Alison Lee
# IntroCS2 pd8
# HW36 -- Put Your Plan Into Action
# 2016-04-20

import random

"""
Mechanism for Madlibification:
    Have word[randrangelenword))] run everytime a word needs
to be inputed. We would have lists with nouns, verbs, adjectives, and adverbs,
and each time one needed to be called, we would have a random index found,
and therefore a random word is chosen from the list. We would then have it
returned. The input for the function is the list of nouns, verbs, adjectives,
and adverbs.

V1 - string split, list of nouns etc., replace, recombining/joining, sentence
"""

nouns = [ "cereal" , "mango" , "mouse" , "box" , "chair" , "knife" , \
"guillotine" , "bat" , "pepper" , "clip" , "earring" , "clock" , "dream" , \
"switch" , "bacterium" , "pomengranate" , "head" , "book" , "animal" , "soap" , \
"bleach" , "chicken" ]

verbs = ['eats', 'sits', 'reads', 'plays', 'moves', 'sleeps', 'arrives', \
         'lies', 'sneezes', 'dies', 'cracks', 'crackles', 'divides', 'drains', \
         'oozes', 'paints', 'pays', 'relaxes', 'shivers', 'talks', 'sails', \
         'turns', 'twists', 'watches', 'eats', 'kills', 'attacks', 'chops', \
         'kicks', 'slaps', 'pushes', 'puts', 'calls', 'opens', 'closes', \
         'holds', 'hugs', 'strokes', 'stirs', 'shakes']

adjectives = ['cute', 'small', 'tall', 'huge', 'tiny', 'ugly', 'fat', 'skinny', \
'white', 'black', 'annoying', 'boring', 'aggresive', 'ambitious', 'helpful', \
'honest', 'knowledgeable', 'witty', 'amused', 'lively', 'anxious', 'wicked']

adverbs = ['quickly', 'slowly', 'beautifully', 'wickedly', 'accidentally', \
'awkwardly', 'boldly', 'coyly', 'deliberately', 'finally', 'innocently', \
'seriously', 'wearily', 'crazily', 'foolishly', 'kindly', 'poorly', 'shakily', \
'technically'] 

sentence = "The <ADJECTIVE> <NOUN> <ADVERB> <VERB>."

def chooseRand( L ) :
    return L[ random.randrange( len( L )) ] 

def fillBlanks( story ) :
    """ 0 - splits the sentence into words and each word is put into a list.
        1 - there will be a while loop that will check each element.
        2 - A random word will be chosen for the corresponding element. The
            placeholder will be replaced.
        3 - After the while loop is done with the entire list, join will be
            used to "convert" it back into a string, which is printed. """
    storyL = story.split( " " )
    i = 0
    while i < len( storyL ) :
        if storyL[ i ] == "<NOUN>" :
            storyL[ i ] = storyL[ i ].replace( storyL[ i ] , chooseRand( nouns ))
        if storyL[ i ] == "<ADJECTIVE>" :
            storyL[ i ] = storyL[ i ].replace( storyL[ i ] , chooseRand( adjectives ))
        if storyL[ i ] == "<ADVERB>" :
            storyL[ i ] = storyL[ i ].replace( storyL[ i ] , chooseRand( adverbs ))
        if storyL[ i ] == "<VERB>" :
            storyL[ i ] = storyL[ i ].replace( storyL[ i ] , chooseRand( verbs ))
        i += 1
    storyS = " ".join( storyL )
    return storyS
    
print fillBlanks( sentence )
# Example result: "The white book wickedly <VERB>." 
# This replaces all the placeholders, except for <VERB>, with the corresponding
# thingy. It doesn't replace <VERB> yet because there is a "." attached to it...


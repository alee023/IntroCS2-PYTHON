#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

# Team Green - Erick Cho & Alison Lee
# IntroCS2 pd8
# HW40 -- Vroom Vrooom WOW!
# 2016-05-04

"""
0  Erick was out for a weeklong vacation so I attempted dealing with punctuation
   myself. I couldn't think of any executable plan and no one could assist so
   my team didn't deal with it at all.
1  I looked at David's code as well as Gilvir's code.
    David's team had a function that added spaces before and the punctuation mark
    while Gilvir's team just didn't have to deal with their punctuation at all -
    it was ignored.
2  While the latter was more efficient, I ended up using David's code because
   Gilvir didn't use a while inside a for loop. 

Mechanism for Madlibification:
    Have word[randrangelenword))] run everytime a word needs
to be inputed. We would have lists with nouns, verbs, adjectives, and adverbs,
and each time one needed to be called, we would have a random index found,
and therefore a random word is chosen from the list. We would then have it
printed. The input for the function is the number of nouns, verbs, adjectives,
and adverbs.

V1 - string split, list of nouns etc., replace, recombining/joining, 1 sentence
V2 - multiple sentences. Attempted to fix punctuation and capitalization.

V3* - fixed punctuation 
"""

import random

nouns = [ 'cereal' , 'mango' , 'mouse' , 'box' , 'chair' , 'knife' , \
'guillotine' , 'bat' , 'pepper' , 'clip' , 'earring' , 'clock' , 'dream' , \
'switch', 'bacterium' , 'pomengranate' , 'head' , 'book' , 'animal' , 'soap' , \
'bleach' , 'chicken' , 'soup' , 'man' , 'kid']

verbs = ['eats', 'sits', 'reads', 'plays', 'moves', 'sleeps', 'arrives', \
'lies', 'sneezes', 'dies', 'cracks', 'crackles', 'divides', 'drains', 'oozes', \
'paints', 'pays', 'relaxes', 'shivers', 'talks', 'sails', 'turns', 'twists', \
'watches', 'kills', 'attacks', 'chops', 'kicks', 'slaps', 'pushes', \
'puts', 'calls', 'opens', 'closes', 'holds', 'hugs', 'strokes', 'stirs', 'shakes']

adjectives = ['cute', 'small', 'tall', 'huge', 'tiny', 'ugly', 'fat', 'skinny', \
'white', 'black', 'annoying', 'boring', 'aggresive', 'ambitious', 'helpful', \
'honest', 'knowledgeable', 'witty', 'amused', 'lively', 'anxious', 'wicked']

adverbs = ['quickly', 'slowly', 'beautifully', 'wickedly', 'accidentally', \
'awkwardly', 'boldly', 'coyly', 'deliberately', 'finally', 'innocently', \
'seriously', 'wearily', 'crazily', 'foolishly', 'kindly', 'poorly', 'shakily', \
'technically']

blanks = [ "<NOUN>" , "<ADJECTIVE>" , "<ADVERB>" , "<VERB>" ]
punc = [ "." , "," , ":" , "..." , "/" , "?" , "!" ]

def puncSpace( s ) :
    # adopted from David's and Andrew's group
    i = 0
    while i < len( s ) :
        if s[i] in punc :
            s = s[ : i ] + " " + s[ i : ]
            i += 1
        i += 1
    return s

def recomb( s ) :
    i = 0
    while i < len( s ):
        if s[ i ] in punc:
            s = s[ : i - 1 ] + s[ i : ]
            i -= 1
        i += 1
    return s

def chooseRand( L ) :
    return L[ random.randrange( len( L )) ]

def madLibify( story ) :
    puncSpaced = puncSpace( story )
    storyL = puncSpaced.split( " " )
    for i in blanks:
        while i in storyL :
            if i == '<NOUN>' :
                storyL[ storyL.index( i ) ] = chooseRand( nouns )
            if i == '<VERB>':
                storyL[ storyL.index( i ) ] = chooseRand( verbs )
            if i == '<ADJECTIVE>' :
                storyL[ storyL.index( i ) ] = chooseRand( adjectives )
            if i == '<ADVERB>' :
                storyL[ storyL.index( i ) ] = chooseRand( adverbs )
    result = recomb(( " ".join( storyL )).capitalize( ))
    for n in result :
        # supposed to capitalize the "i"s in the result but doesn't work here for some reason.
        if (( n == "i" ) and ( result[ result.index( n ) - 1 ] == " " ) and ( result[ result.index( n ) + 1 ] == " " )) :
            result = result[ : result.index( n ) ] + "I" + result[ result.index( n ) + 1 : ]
    return result


story = 'She <VERB> on the table, leading to a <ADJECTIVE> reply from her parents. \
Why did you do that you <NOUN>... you <ADJECTIVE> <NOUN>?!?!\
 I do not know, I was <ADJECTIVE> - maybe I am just tired.\
 Now he <VERB> because of you, I knew that she <VERB> for you.\
 She left the <ADJECTIVE> room, reading the newspaper. The headline today was\
<ADJECTIVE> <NOUN> begins to <ADVERB> split. '

print madLibify( story )

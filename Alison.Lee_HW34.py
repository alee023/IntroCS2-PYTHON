# Alison Lee
# IntroCS2 pd8
# HW34 -- Oh, Give Me a Home Where the Buffalo Roam (Home on the Range ;)))
# 2016-04-18

import random

# 1
def remAll( L, item ):
    """ This function removes all occurrences of 'item' from 'L' """
    result1 = [ ]
    for n in L :
        if n != item:
            result1.append( n )
    return result1

def merge( L1 , L2 ) :
    """ Combines L1 and L2 in one list. It then takes the minimum of this list
        and adds it onto the result. """
    list2 = L1 + L2
    result2 = [ ]
    while len( list2 ) > 0 :
    # list2 grows shorter each time as the min is removed from it. 
        result2.extend( list2.count( min( list2 )) * [ min( list2 ) ] )
        # there might be several minimums 
        list2 = remAll( list2 , min( list2 ))
        # removing the minimum
    return result2
    
    
a = [ 0 , 3 , 4 , 9 , 11 ]
b = [ 2 , 3 , 6 , 12 ]
print merge( a , b )
# [ 0 , 2 , 3 , 3 , 4 , 6 , 9 , 11 , 12 ]

# 2
def randList( n ) :
    """ As each random number is added onto the list, 1 is subtracted from n.
        Therefore only n elements would be in the resulting list. """
    result = [ ]
    while n > 0 :
        result.append( random.randrange( 100 ))
        n -= 1
    return result

print randList( 5 )
# [ ? , ? , ? , ? , ? ]
print randList( 3 )
# [ ? , ? , ? ]

# 3
def rand256( ) :
    return random.randrange( 256 )

def randIPv4( ) :
    """ IPv4 address: [0-255].[0-255].[0-255].[0-255] """
    return str( rand256( )) + "." + str( rand256( )) + "." \
           + str( rand256( )) + "." + str( rand256( ))

print randIPv4( )
# ???.???.???.???

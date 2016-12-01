# Alison Lee
# IntroCS2 pd8
# HW32 -- Stats on Stats on Stats
# 2016-04-14

def findMost( L ) :
    """ finds the number of occurrences of each element in a list and
    finds the max of those. In other words, it finds the number of times
    the mode appears in the given list. """
    num = L.count( L[ 0 ] )
    for n in L :
        num = max( num , L.count( n ))
    return num

def modeListA( L ) :
    """ returns the mode in integer form. If there are multiple modes, it
    returns the 1st one that it encounters only """
    for n in L :
        if findMost( L ) == L.count( n ) :
            return n

print modeListA( [ 1 , 2 , 3 , 2 , 5 , 2 ] ) # 2
print modeListA( [ 1 , 3 , 2 , 3 , 2 , 0 ] ) # 3

def BHelper( L ) :
    """ This is a helper function that will return ALL the numbers with
    the same number of occurrences as the number returned by findMost.
    Since it returns all the numbers, there might be repeated values in the
    list it returns. """
    result = [ ]
    for n in L :
        if findMost( L ) == L.count( n ) :
            result.append( n )
    return sorted( result )

def modeListB( L ) :
    """ Deceiving function name // this one just removes the duplicates
    in the list that BHelper returns """
    index = 0
    mode = BHelper( L )
    while index < len( mode ) :
        if mode.count( mode[ index ] ) > 1 :
             mode = mode[ : index + 1 ] + \
                    mode[ index + mode.count( mode[ index ] ) : ]
             # will keep the orig number 
             # and the number afterrr the duplicates
        else :
             index += 1
    return mode
print modeListB( [ 1 , 2 , 3 , 2 , 5 , 2 ] ) # [ 2 ]
print modeListB( [ 1 , 2 , 3 , 3 , 2 , 0 ] ) # [ 2 , 3 ]
print modeListB( [ 1 , 2 , 3 , 4 , 3 , 2 , 1 ] ) # [ 1 , 2 , 3 ]

def sub1( L ) :
    index = 0
    while index < len( L ) :
        if L[ index ] >= 1 :
            L[ index ] = L[ index ] - 1
        else :
            L[ index ] = 0
        index += 1
    return L
    
def xaxis( L ) :
    result = ""
    for n in L :
        result += str( L.index( n )) + " "
    return result
    
def spacify( s ) :
    result = ""
    for w in s :
        result += str( w ) + " " 
    return result
    
def onify( L ) :
    result = [ ] 
    for n in L :
        if n > 0 :
            result.append( 1 )
        else :
            result.append( 0 )
    return result
    
def starify( L ) :
    result = ""
    List = onify( L )
    for n in List :
        if n > 0 :
            result += n * "*"
        else :
            result += " " 
    return result

def vBarGraphify( L ) :
    """ Will create a string that is built from the bottom to the top using
        a loop. At the end, the 'x-axis' is added to the bottom, going from
        0 -> len( L ) - 1 """
    dupL = [ ]
    dupL.extend( L )
    maxList = max( dupL )
    newString = ""
    index = 0
    while maxList > 0 :
        newString = spacify( starify( dupL )) + "\n" + newString
        dupL = sub1( dupL )
        maxList = max( dupL )
    newString += xaxis( L )
    print newString
    
vBarGraphify( [ 0 , 1 , 2 , 3 ] )
vBarGraphify( [ 1 , 0 , 3 , 2 ] )

    

        
    

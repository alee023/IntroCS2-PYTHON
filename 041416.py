# Alison Lee
# IntroCS2 pd8
# 2016-04-14

def findMost( L ) :
# finds the number of occurrences of each element in a list and
# finds the max of those. In other words, it finds the number of times
# the mode appears in the given list.
    num = L.count( L[ 0 ] )
    for n in L :
        num = max( num , L.count( n ))
    return num

def modeListA( L ) :
# returns the mode in integer form. If there are multiple modes, it
# returns the 1st one that it encounters only
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
    """ Deceiving function name // this one just deletes those extra values
    in the list that BHelper returns """
    index = 0
    mode = BHelper( L )
    while index < len( mode ) :
        if mode.count( mode[ index ] ) > 1 :
             mode = mode[ : index + 1 ] + \
                    mode[ index + mode.count( mode[ index ] ) : ]
        else :
             index += 1
    return mode
print modeListB( [ 1 , 2 , 3 , 2 , 5 , 2 ] ) # [ 2 ]
print modeListB( [ 1 , 2 , 3 , 3 , 2 , 0 ] ) # [ 2 , 3 ]
print modeListB( [ 1 , 2 , 3 , 4 , 3 , 2 , 1 ] ) # [ 1 , 2 , 3 ]

# Alison Lee
# IntroCS pd8
# HW33 -- Bucket List
# 2016-04-15

def buckets( L ) :
# will create a list that will order the numbers in L into "buckets"
    buckets = ( max ( L ) + 1 ) * [ 0 ]
    # 1 - creates a list that is max( L ) + 1 elements long and
    # 2 - makes all the elements 0
    for n in L :
        buckets[ n ] += 1
        # counts the frequency of each element in L
    return buckets

def findMode( L ) :
# will return the index(es) of the max of the frequencies found by buckets( L )
# note that the index of bucketList elements are the elements of L 
    bucketList = buckets( L )
    maxList = max( bucketList )
    mode = [ ]
    index = 0
    while index < len( bucketList ) :
        if bucketList[ index ] == maxList :
            mode.append( index )
            # appends the index (or mode) to the result list
        bucketList[ index ] = 0
        # will set the previous bucketList[ index ]s to 0 to prevent errors
        # from occurring when there are several modes
        index += 1
    return mode 
    
print findMode( [ 0 , 3 , 0 , 2 , 3 ] ) # [ 0 , 3 ]
print findMode( [ 1 , 2 , 3 , 2 , 2 ] ) # [ 2 ]
print findMode( [ 1 , 2 , 3 , 1 , 1 ] ) # [ 1 ]

# ---------

def sub1( L ) :
# subtracts 1 from each element in L, unless that element is 0
    index = 0
    while index < len( L ) :
        if L[ index ] >= 1 :
            L[ index ] = L[ index ] - 1
        else :
            L[ index ] = 0
        index += 1
    return L
    
def xaxis( L ) :
# prints out the x-axis of the bar graph
    result = ""
    for n in L :
        result += str( L.index( n )) + " "
    return result

def onify( L ) :
# returns a list of ones and zeros. If n is a nonzero number, it appends 1 to
# the result list. Otherwise it appends 0.
    result = [ ] 
    for n in L :
        if n > 0 :
            result.append( 1 )
        else :
            result.append( 0 )
    return result
    
def starify( L ) :
# will return one row of the vertical bar graph. A '1' in the "onified"
# list means a star and a '0' means an empty space
    result = ""
    List = onify( L )
    for n in List :
        if n > 0 :
            result += n * "*" + " "
        else :
            result += "  " 
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
        newString = starify( dupL ) + "\n" + newString
        dupL = sub1( dupL )
        maxList = max( dupL )
    newString += xaxis( L )
    print newString
    
vBarGraphify( [ 0 , 1 , 2 , 3 ] )
#       *
#     * *
#   * * *
# 0 1 2 3
vBarGraphify( [ 1 , 0 , 3 , 2 ] )
#       *  
#     * *
# *   * *
# 0 1 2 3

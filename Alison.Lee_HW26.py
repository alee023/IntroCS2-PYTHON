# Alison Lee
# IntroCS2 pd8
# HW26 -- Float Like a Butterfly, Sting Like a Bee
# 2016-04-04

def findMin( a , b ):
    # This returns the minimum of 2 numbers. Basically the min() function
    if a > b :
        return b
    elif a < b :
        return a
    else :
        return a

def minList( L ) :
    # This function compares 2 numbers at a time. It stores the minimum of
    # those 2 numbers in a variable called result. result is then compared
    # to the next number in the list and result is redefined as the minimum
    # of that. 
    index = 0
    # so that it starts at the beginning of the list
    result = L[ 0 ]
    # it's a bad idea to set result to 0 because it will always stay 0.
    # I therefore set it to the first element. 
    while index < len( L ) :
        result = findMin( result , L[ index ] )
        # finds the minimum between the minimum (result) so far (it will be
        # the first element when it first runs) and an element in the list
        # (which will also be the first element when it first runs)
        index += 1
    return result

def minPos( L ) :
    # I had 2 helper functions. This one will just return the position of
    # the lowest value found with minList( L ).
    return L.index( minList( L ))

print minPos( [ 1 , 2 , 3 , 4 , 5 ] )
# should return 0
print minPos( [ 5 , 4 , 3 , 2 , 1 ] )
# should return 4
print minPos( [ 3 , 1 , 4 , 5 , 2 , 9 ] )
# should return 1
print minPos( [ 6 , 7 , 1 , 2 , 1 ] )
# special case where there are 2 minimums. Should return the first
# occurrence, which is at 2


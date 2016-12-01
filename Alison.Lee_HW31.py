# Alison Lee
# IntroCS2 pd8
# # HW31 -- Stat-tastic
# 2016-04-14

# 1
def meanList( nums ) :
    sumL = 0
    for n in nums :
    # using for because you are finding the sum of EVERY element in the list
        sumL += n
        # an element is added to the sum of the previous ones
    return sumL / len( nums )
    # an arithmetic mean is the sum of numbers / # of numbers provided

print meanList( [ 1 , 2 , 3 ] ) # 2
print meanList( [ 3 , 5 , 2 , 1 , 4 ] ) # 3

# 2
def medList( nums ) :
    nums = sorted( nums )
    if len( nums ) % 2 == 0 :
        return ( nums[ len( nums ) / 2 - 1 ] + nums[ len( nums ) / 2 ] ) / 2.0
        # nums[ len( nums ) / 2 - 1 ] is the last number in the first half
        # nums[ len( nums ) / 2 ] is the first number in the last half
    else :
        return nums[ len( nums ) / 2 ]
        
print medList( [ 4 , 2 , 1 , 3 ] ) # 2.5
print medList( [ 3 , 2 , 5 , 1 , 4 ] ) # 3

# 3
def barGraphify( nums ) :
    result = ""
    for n in nums :
        result += str( nums.index( n )) + ": " + ( n * "=" ) + "\n" 
    print result

barGraphify( [ 0 , 1 , 2 , 3 ] )
# 0: 
# 1: =
# 2: ==
# 3: ===
barGraphify( [ 1 , 0 , 3 , 2 ] )
# 0: =
# 1:
# 2: ===
# 3: ==



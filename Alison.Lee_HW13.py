#Alison Lee
#IntroCS2 pd8
#HW13 -- The Handoff
#2016-03-10

import math
    # to be used in #2

#1
def numRealRoots ( a , b , c ):
    # uses the discriminant // b^2 - 4ac
    if ( b ** 2 ) - ( 4 * a * c ) > 0 :
        return 2
    # 2 roots if the discrimant evaluates to a positive number
    elif ( b ** 2 ) - ( 4 * a * c ) == 0 :
        return 1
    # 1 root if it evaluates to 0
    else :
        return 0
    # 0 roots otherwise / if it evaluates to a negative number

# numRealRoots ( 1 , 2 , 3 ) should return 0
# numRealRoots ( 2 , 4 , 2 ) should return 1
# numRealRoots ( 1 , 3 , 2 ) should return 2

#2
def quadSolver ( a , b , c ) :
    # utilizes the quadratic formula for the quadratic equation
    # ax^2 + bx + c = 0
    if numRealRoots ( a , b , c ) == 2 :
        return (((( -1 * b ) + math.sqrt(( b ** 2 ) - ( 4 * a * c ))) / ( 2 * a ))
        # returns posRoot
        , ((( -1 * b ) - math.sqrt(( b ** 2 ) - ( 4 * a * c ))) / ( 2 * a )))
        # returns negRoot
    elif numRealRoots ( a , b , c ) == 1 :
        return ((( -1 * b ) + math.sqrt(( b ** 2 ) - ( 4 * a * c ))) / ( 2 * a ))
    else :
        return "No real roots"

# quadSolver ( 1 , 2 , 3 ) should return "No real roots"
# quadSolver ( 1 , 4 , 4 ) should return -2
# quadSolver ( 1 , -2 , -15 ) should return ( 5.0 , -3.0 )
    # Wasn't sure how to display multiple results

#Alison Lee
#IntroCS pd8
#HW10 -- Visiting Old Friends
#2016-3-7

import math

#1
def areaCirc ( r ):
    return math.pi * ( r ** 2.0 )
# areaCirc ( 1 ) returns pi: 3.14159265...
# areaCirc ( 3 ) returns 28.274333...

#2
def areaWasher ( radInner , radOuter ):
    return ( math.pi * ( radOuter ** 2.0 )) - ( math.pi * ( radInner ** 2.0 ))
# areaCirc ( 2, 5 ) returns 65.9734457...
# areaCirc ( 3, 5 ) returns 50.265482457...

#3
def sumOfSquares ( a , b ):
    return ( a ** 2 ) + ( b ** 2 )
# sumOfSquares ( 1 , 5 ) returns 26
# sumOfSquares ( 1 , 3 ) returns 10



# Alison Lee
# IntroCS2 pd8
# HW20 -- Reaching out to neighbors
# 2016-03-24

def closerNum ( target , num1 , num2 ) :
    diff1 = abs( num1 - target )
    # finds the difference between num1 and target
    diff2 = abs( num2 - target )
    # diff btwn num2 and target
    if diff1 > diff2 :
        # if diff1 > diff2, num2 is closer to target
        return str( target ) + " is closer to " + str( num2 )
    elif diff1 == diff2 :
        # meaning neither one is closer...
        return "Neither " + str( num1 ) + " or " + str( num2 ) + " is closer to " + str( target )
    else :
        # diff1 < diff2 // num1 is closer
        return str( target ) + " is closer to " + str( num1 )

print closerNum( 8 , 20 , 10 )
print closerNum( 8 , 20 , 2 )
print closerNum( 8 , -2 , 30 )
print closerNum ( 8 , 0 , 16 )

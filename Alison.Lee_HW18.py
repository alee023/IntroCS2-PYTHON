# Alison Lee
# IntroCS2 pd8
# HW18 -- 000 000 111 v. 2
# 2016-03-21

def bondify ( name ) :
    space = name.find( " " )
    first = name[ space + 1 : ]
    # all the characters before the space make up the FIRST name and
    last = name[ : space ]
    # the characters after the space make up the LAST name
    return first + ", " + last + " " + first

print bondify( "James Bond" )
# should return "Bond, James Bond"

def replace ( s , q , r ) :
    a = s.find( q )
    b = len( q )
    if a != -1 :
    # meaning "if q is present in s"
        return s[ : a ] + r + s[ ( a + b ) : ]
        # it should keep the characters BEFORE q and the ones AFTER Q.
        # r replaces q 
    else :
    # and if q isn't found anywhere in s, the original sentence is kept
        return s

print replace ( "Winter is coming" , "Winter" , "Spring" )
# should print "Spring is coming" 
print replace ( "Dolphins run this planet" , "dolphins" , "mice" )
# should print "Dolphins run this planet" <-- no change
print replace ( "What are you up to" , "are you" , "is he" )
# should print "What is he up to"


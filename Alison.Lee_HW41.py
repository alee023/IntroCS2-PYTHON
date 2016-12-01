#!/usr/bin/python
print "Content-Type: text/html\n"
print ""
print "<!DOCTYPE html> <html>"
# Team Cocoa Puffs - Fabiola Radosav, Alison Lee
# IntroCSpd8
# HW41 -- ASCIIing About Your Visage
# 2016-05-05

import random

# 1
def common( L1 , L2 ) :
    result = [ ]
    for n in L1 :
        if n in L2 :
        # n is definitely in L1 but if n is in L2 as well...
            result.append( n )
            # it is appended onto the result list
    return sorted( result )

print common( [ 1 , 5 , 4 , 3 , 2 ] , [ 4 , 5 , 10 , 15 ] )
# [ 4 , 5 ]

# 2
def alphabetize( names ) :
    """ When one's last name is at the beginning of "names", there should
        be an odd amount of spaces. That variable mentioned above will store
        the last name AND the space after it. Those are also removed from
        "names" so that person's first name is at the front of "names". There
        will be an even amount of spaces then. This first name is added onto the
        aforementioned variable, which should now store the last and first name.
        The string that this variable stores is appended onto a list that stores
        names. This continues until "names" is empty. """
    LF = ""
    # will store ONE person's last and first name
    namesL = [ ]
    # stores names (LFs)
    names = names.replace( "," , " " )
    # the resulting names each have a space btwn the first and last
    # name so I changed all the commas to space ahead of time
    while len( names ) > 0 :
    # the string "names" gets shortened so the while loop stops
    # running when it's empty
        if  names.count( " " ) > 0 :
            i = names.index( " " )
            if names.count( " " ) % 2 == 1 :
            # the way my code is run, an odd amt of spaces indicates that
            # a last name is at the beginning of list names
                LF = names[ : i + 1 ]
                # name-storing-variable will store the last name AND a space
                names = names[ i + 1 : ]
                # names is shortened. A first name is at the front now
            else :
            # even amt of spaces. This means that the first name is at the front
            # of names, meaning that this part of the code should run right after
            # the above code
                LF += names[ : i ]
                # the first names get added onto the last name in LF
                namesL.append( LF )
                # now LF stores both the last and first name. It can then be
                # added onto namesL
                names = names[ i + 1 : ]
                # shortens names again. The next person's last name is at the
                # front of names
        else :
        # there aren't any more spaces by now but the last person's first name
        # still remains in names. We can just append this remaining part onto LF
        # and add it onto namesL
            LF += names
            namesL.append( LF )
            names = ""
    # right now, namesL looks like
    # [ <last> <first>, <last> <first>, and so on ]
    # note that the last names are not alphabetized yet and we can do this
    # with sorted     vvvvvv
    return "\n".join( sorted( namesL ))

print alphabetize( "Wayne,Bruce,Kent,Clark,Parker,Peter" )
# Kent Clark
# Parker Peter
# Wayne Bruce

# 3
print "<h3> RANDOM ASCII FACE GENERATOR </h3> <pre> <font size=14>"

hair = [ "|" , "#" , "*" , "@" , "/" , "^" , "S" ]
eyes = [ "^" , "v" , "*" , "@" , "x" , "=" , "." , "$" , ">" , "<" ]
nose = [ "_" , "U" , "V" , "-" ]
mouth = [ "\_/" , "___" , "vvv" , " ^ " , " * " , "~~~" ]
    
def rand( L ) :
    return L[ random.randrange( len( L )) ]

def face( ) :
    print 11 * rand( hair )
    print "|         |"
    print "|  " + rand( eyes ) + "   " + rand( eyes ) + "  |"
    print "|    " + rand( nose ) + "    |"
    print "\   " + rand( mouth ) + "   /"
    print " \_______/"

face( )
print "</font> </pre> </html>"



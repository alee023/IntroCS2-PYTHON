#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

# Alison Lee
# IntroCS2 pd8
# HW53 -- GET Some Computation Done
# 2016-05-24

import os
d = os.environ

qs = d[ "QUERY_STRING" ]
qs = qs.split( "&" )

a = qs[ 0 ]
b = qs[ 1 ]
c = qs[ 2 ]

a = int( a[ 2 ] )
b = int( b[ 2 ] )
c = int( c[ 2 ] )

perim = a + b + c

def area( s1 , s2 , s3 ) :
    s = 0.5 * ( s1 + s2 + s3 )
    s1 = s - s1
    s2 = s - s2
    s3 = s - s3
    return ( s * s1 * s2 * s3 ) ** 0.5

print "In a triangle with side lengths " + str( a ) + ", " + str( b ) \
+ ", and " + str( c ) + ", the perimeter is " + str( perim ) + " and the area i$
+ str( area( a , b , c )) + "."

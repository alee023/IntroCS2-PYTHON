#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import cgi
import cgitb
cgitb.enable( )
query = cgi.FieldStorage( )

def FStoD():
    d = {}
    for k in query.keys():
        d[k] = query[k].value
    return d
d = FStoD( )
keys = d.keys()
values = d.values()

def rot13Chr( ch ) :
    if ch.upper() == ch :
        offset = ord( 'A' )  #65
    else :
        offset = ord( 'a' )  #97
    if (( ch == " " ) or ( ord( ch ) < 65 ) \
        or (( 90 < ord( ch ) < 97 )) \
        or ( ord( ch ) > 122 )) :
        result = ch
    else :
        result = chr(( ord( ch ) + 13 - offset ) % 26  + offset )
    return result

def rot13( value ) :
    newPhrase = ""
    for n in value :
        newPhrase += rot13Chr( n )
    return newPhrase

def reverse( value ) :
    newPhrase = ""
    index = -1
    while len( newPhrase ) < len( value ) :
        newPhrase += value[ index ]
        index -= 1
    return newPhrase

def todo( ) :
    index = keys.index( "word" )
    value = values[ index ]
    if values[ -1 ] == "ROT13" :
        rot13( value )
    else :
        reverse( value )

htmlStr = "Content-Type: text/html\n\n"
htmlStr += "<html>"
htmlStr += todo( )
htmlStr += "</html>"

print htmlStr


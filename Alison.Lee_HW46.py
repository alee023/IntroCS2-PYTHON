#!/usr/bin/python
print "content-type: text/html\n"
print ""

"""
Team Cali - Connie Lei, Alison Lee
IntroCS2 pd8
HW46 -- Maxim:Don't timeout and don't get sued.
2016-05-11
"""

lit = open( "lit.txt" , "r" )
text = lit.read()
lit.close()

def stringfy(txt):
    tally = { }
    inputL = txt[662:563017]
    inputL = txt.lower()
    inputL = inputL.split()
    return len(inputL)

length = stringfy(text)

blacklist = "the us most day give the be too of and a in that have i it for not on with he as \
 you do at this but his by from they we say her she or an will my one all would there their what so \
up out if about who get which go me when make can like time no just yes know take people into see \
other look only also think most first even want use after is were must could man him upon am shall \
had to said your our some over very should may am upon ".split() + ['back','down','are','any','before','two','been','how','much','has','was','more','then','the\
m','here','now','come','than','might','well','matter','where','came']

def stringfyTheTally(txt):
    tally = { }
    inputL = txt[662:563017]
    inputL = txt.lower()
    inputL = inputL.split()
    for word in inputL:
        newW = word.strip('".?,:!;\n')
        if ( not newW in blacklist ) and ( newW in tally ) :
            tally[ newW ] += 1
        elif not newW in blacklist :
            tally[ newW ] = 1
    return tally

tally = stringfyTheTally( text )

def topn( d , n ) :
    finalDN = { }
    key = d.keys()
    value = d.values()
    while n > 0 :
        tempV = value.index( max( value ))
        finalDN[ key[ tempV ] ] = max( value )
        del value[ tempV ]
        del key[ tempV ]
        n -= 1
    return finalDN

def sortedDict(dictionary):
    value = dictionary.values()
    key = dictionary.keys()
    sortedKey = []
    sortedValue = []
    while len(key) > 0:
        maxPos = value.index(max(value))
        sortedKey.append(key[maxPos])
        del key[maxPos]
        sortedValue.append((max(value)))
        del value[maxPos]
    return [sortedKey,sortedValue]
    
print '<!DOCTYPE html> \n<html> \n<body style="text-align:center">'
print "<h2><b> The Adventures of Sherlock Holmes </b></h2>"
print '<a href="lit.txt">Full Story</a>'

def tablefy( d ):
    print "<table border = '1'> \n<r> <td> Top 30 Most Common Words </td></r> \n<tr> \
<td> Word </td> <td> Frequency </td> <td> Percentage </td></tr>"
    keys = d[0]
    values = d[1]
    for i in keys :
        iPos = keys.index(i)
        print "<tr> <td> " + str( i ) + " </td> <td> " + str( values[iPos] ) \
              + " </td> <td> " + str( float( values[iPos] ) / length * 100 ) + "% </td> </tr>" 
    print "</table>"

print "<h2> Blacklist of Common Words</h2> \n<p>" + (" ").join(blacklist) + "</p>"

htmlInput = topn(tally,30)
tablefy(sortedDict(htmlInput))

print '</body> \n</html>'

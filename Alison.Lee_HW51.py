# Team  - Alison Lee, Fabiola Radosav, Kaia Tien
# IntroCS2 pd8
# HW51 -- Present Your Findings
# 2016-05-20

"""
0 - Function that takes the readline version of the csv file and returns a list
    with sublists
1 - Isolate the data we need: # of Test Takers
2 - Function that takes the DBN values from one csv file and tries to find
    it in the other. If it is present, then we can put the # of Test Takers
    data in separate (parallel lists). The DBN that is in common would be in a
    list as well.
        HW41 - common( L1 , L2 ) which returns a list (for DBN)
        Find the index of that DBN in that list we just created and use that
        index to find and append the # of Test takers to a list
3 - Sort
4 - Tablefy function
"""

s = open( "SAT_Results.csv" , "r" )
sRL = s.readlines()
s.close()
# sat = 6 columns, ap = 5 columns. Keeping first and third of each
a = open( "AP__College_Board__2010_School_Level_Results.csv" )
aRL = a.readlines()
a.close()

def listify( L , n ) :
    # n should be either 5 or 6
    # it doesn't "fix" the comma problem. It deletes some things we don't need
    for i in L :
        p = L.index( i )
        L[ p ] = L[ p ].strip()
        L[ p ] = L[ p ].split( "," )
        subEl = L[ p ]
        while len( subEl ) > n :
            del subEl[ 1 ]
    return L

sL = listify( sRL , 6 )
aL = listify( aRL , 5 )

def Lcol( L , column ) :
    # takes listified version of a list
    coL = [ ]
    for i in L[ 1 : ] :
        el = i[ column ]
        coL += [ el ]
    return coL

s1 = Lcol( sL , 0 )
a1 = Lcol( aL , 0 )
SAT = Lcol( sL , 2 )
AP = Lcol( aL , 2 )
    
def common( ) :
    # looks for things in common in Lcol( aL/sL , 0 ) to get the common DBNs
    result = [ ]
    for n in s1 :
        if n in a1 :
            result.append( n )
    return result

DBN = common( )

def getN( n ) :
    # takes 1 or 2 as the input, 1 being for SAT and 2 for AP
    # uses the DBN list, finds the index of each DBN in s1 and a1. Uses that index
    # to find the # of test takers in SAT and AP. Returns lists based on n
    if n == 1 :
        a = s1
        b = SAT
    else :
        a = a1
        b = AP
    result = [ ]
    for i in DBN :
        pos = a.index( i )
        result.append( b[ pos ] )
    return result

SAT = getN( 1 )
AP = getN( 2 )

"""
def sI( L ) :
    result = [ ]
    for n in L :
        if n == "s" :
            result.append( n )
        else :
            # n is a number
            result.append( int( n ))
    return result
    
sortedSAT = sorted( sI( SAT ))
"""
"""
def sortL( n ) :
    # returns a list that corresponds w/ sorted SAT values
    # goes through sortedSAT, finds the index of each in getN( 1 ) and
    # uses that index in getN( 2 )
    # n = 1 -> returns "sorted" DBNs, 2 returns "sorted" AP
    resL = [ ]
    if n == 1 :
        a = DBN
    else :
        a = sI( AP )
    for n in sortedSAT :
        pos = sI( SAT ).index( n )
        resL.append( a[ pos ] )
    return resL
"""
def tablefy( ) :
    # col1 = sortL( DBN ) , col2 = SAT , col3 = AP 
    n = 0
    print "<html> <table border = '1'> \n" 
    print "<tr> <td> DBN </td> <td> # of SAT Takers </td> <td> # of AP Exam Takers </td> </tr> \n" 
    while n < 253 :
        print "<tr> <td> " + DBN[ n ] + " </td> <td> " + SAT[ n ] \
                 + " </td> <td> " + AP[ n ] + " </td> </tr>"
        n += 1
    print "</table> </html>" 

tablefy()


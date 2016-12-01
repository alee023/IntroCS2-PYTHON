# Team  - Alison Lee, Fabiola Radosav, Kaia Tien
# IntroCS2 pd8
# HW51 -- Better Code Through Incremental Revision
# 2016-05-26

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
3 - Tablefy function

MODIFICATIONS: Added links...
"""

s = open( "SAT_Results.csv" , "r" )
sRL = s.readlines()
s.close()
a = open( "AP__College_Board__2010_School_Level_Results.csv" )
aRL = a.readlines()
a.close()

def listify( L , n ) :
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
    result = [ ]
    for n in s1 :
        if n in a1 :
            result.append( n )
    return result

DBN = common( )

def getN( n ) :
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

def tablefy( ) :
    n = 0
    print "<html> <li> <a href='AP__COLLEGE_Board__2014_School_Level_Results.csv'> AP </a> </li>"
    print "<li> <a href='SAT_Results.csv'> SAT </a> </li>"
    print "<table border = '1'>"
    print "<tr> <td> DBN </td> <td> # of SAT Takers </td> <td> # of AP Exam Takers </td> </tr>" 
    while n < 253 :
        print "<tr> <td> " + DBN[ n ] + " </td> <td> " + SAT[ n ] \
                 + " </td> <td> " + AP[ n ] + " </td> </tr>"
        n += 1
    print "</table> </html>" 

tablefy()


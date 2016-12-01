# Alison Lee
# IntroCS2 pd8
# HW49 -- How Many Numbers Could a Thinker Crunch, if a Thinker Could Crunch
# 2016-05-17

"""
I added functions to find the mean, median, high, and low for the numerical
data. The return values for these functions were used in a table that displays
this data.
"""

f = open( "SAT_Results.csv" , "r" )
rL = f.readlines()
f.close()

w = open( "hw48" , "w" )

def listify( L ) :
    for n in L :
        i = L.index( n )
        L[ i ] = L[ i ].strip()
        L[ i ] = L[ i ].split( "," )
        if len( L[ i ] ) == 7 :
            subEl = L[ i ]
            subEl[ 1 ] += "," + L[ i ].pop( subEl.index( subEl[ 2 ] ))
        if len( L[ i ] ) == 8 :
            subEl = L[ i ]
            subEl[ 1 ] += "," + L[ i ].pop( subEl.index( subEl[ 2 ] )) + "," \
                         + L[ i ].pop( subEl.index( subEl[ 2 ] ))
    return L

def tablefy( L ) :
    w.write( "<html> <table border = '1'> \n" )
    for n in L :
        w.write( "<tr> <td> " + n[ 0 ] + " </td> <td> " \
                 + n[ 1 ] + " </td> <td> " + n[ 2 ] + " </td> <td> " \
                 + n[ 3 ] + " </td> <td> " + n[ 4 ] + " </td> <td> " \
                 + n[ 5 ] + " </td> </tr> \n" )
    w.write( "</table> </html>" )

#----------------------------------------------------------------------

def Lcol( L , column ) :
    # takes remn
    coL = [ ]
    for i in L[ 1 : ] :
        el = i[ column ]
        if el != "s" :
            intel = int( el )
            coL += [ intel ]
    return coL

# colums w/ numbers are 2-5 inclusive
def meanC( column ) :
    # L should be remn 
    Sum = 0
    count = 0
    L = Lcol( remn , column )
    for i in L :
        # skips over the first row: DBN, School Name, ...
        Sum += i
        count += 1
    return float( Sum ) / count

def max0min( column , n ) :
    if n == 1 :
        return min( Lcol( remn , column ))
    else :
        return max( Lcol( remn , column ))

def median( column ) :
    L = Lcol( remn , column )
    L = sorted( L )
    if len( L ) % 2 == 0 :
        return ( L[ len( L ) / 2 - 1 ] + L[ len( L ) / 2 ] ) / 2.0
    else :
        return L[ len( L ) / 2 ]

def statTable( ) :
    w.write( "<html> <table border = '1'> \n <tr> <td> </td> "\
             + "<td> Number of SAT Test Takers </td> <td> SAT Critical Reading Average </td> "\
             + "<td> SAT Math Average </td> <td> SAT Writing Average </td> </tr> \n " \
             + "<tr> <td> Mean </td> <td> " + str( meanC( 2 )) + " </td> <td> " + str( meanC( 3 )) \
             + " </td> <td> " + str( meanC( 4 )) + " </td> <td> " + str( meanC( 5 )) + " </td> </tr>" \
             + "<tr> <td> Median </td> <td> " + str( median( 2 )) + " </td> <td> " \
             + str( median( 3 )) + " </td> <td> " + str( median( 4 )) + " </td> <td> " \
             + str( median( 5 )) + " </td> </tr> \n <tr> <td> Low </td> "\
             + "<td> " + str( max0min( 2 , 1 )) + " </td> <td> "\
             + str( max0min( 3 , 1 )) + " </td> <td> " + str( max0min( 4 , 1 )) \
             + " </td> <td> " + str( max0min( 5 , 1 )) + " </td> </tr> \n"\
             + "<td> High </td> <td> " + str( max0min( 2 , 2 )) + " </td> <td> "\
             + str( max0min( 3 , 2 )) + " </td> <td> " + str( max0min( 4 , 2 )) \
             + " </td> <td> " + str( max0min( 5 , 2 )) + " </td> </tr> </table> </html> " )


#----------------------------------------------------------------------

remn = listify( rL )

w.write( "<p> The table directly below displays SAT results for schools in NYC. The table that follows displays statistical info" )

tablefy( remn )

statTable()
w.close()

"""
o = open( "hw48" , "r" )
r = o.read()
print r
o.close()
"""

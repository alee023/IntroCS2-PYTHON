# Alison Lee
# IntroCS2 pd8
# HW47 -- CSV -> HTML
# 2016-05-14

f = open( "testdata.csv" , "r" )
rL = f.readlines()
f.close()

w = open( "hw47" , "w" )

def listify( L ) :
    for n in L :
        i = L.index( n )
        # so that it doesn't have to be typed over and over again
        L[ i ] = L[ i ].strip( "\n" )
        # "\n" is removed from the end of each element in L
        L[ i ] = L[ i ].split( "," )
        # each element in is split by commas. L by this point should be a list
        # with sublists; L[ 0 ] = [ x , x , x ]
    return L

# print listify( r )


def tablefy( L ) :
    w.write( "<html> <table border = '1'> \n" )
    for n in L :
        w.write( "<tr> <td> " + n[ 0 ] + " </td> <td> " \
		+ n[ 1 ] + " </td> <td> " + n[ 2 ] + " </td> </tr> \n" )
    w.write( "</table> </html>" )

remn = listify( rL )
tablefy( remn )
w.close()

"""
o = open( "hw47" , "r" )
r = o.read()
print r
o.close()
"""
# to test if it works (it should)
"""
<html> <table border = '1'> 
<tr> <td> Maasym </td> <td> 999 </td> <td> a </td> </tr> 
<tr> <td> Mahasim </td> <td> 1000 </td> <td> b </td> </tr> 
<tr> <td> Maia </td> <td> 1001 </td> <td> c </td> </tr> 
<tr> <td> Marfark </td> <td> 1002 </td> <td> d </td> </tr> 
<tr> <td> Marfik </td> <td> 1003 </td> <td> e </td> </tr> 
<tr> <td> Markab </td> <td> 1004 </td> <td> f </td> </tr> 
<tr> <td> Matar </td> <td> 1005 </td> <td> a </td> </tr> 
<tr> <td> Mebsuta </td> <td> 1006 </td> <td> b </td> </tr> 
<tr> <td> Media </td> <td> 1007 </td> <td> c </td> </tr> 
<tr> <td> Megrez </td> <td> 1008 </td> <td> d </td> </tr> 
<tr> <td> Meissa </td> <td> 1009 </td> <td> e </td> </tr> 
<tr> <td> Mekbuda </td> <td> 1010 </td> <td> f </td> </tr> 
<tr> <td> Menchib </td> <td> 1011 </td> <td> a </td> </tr> 
<tr> <td> Menkab </td> <td> 1012 </td> <td> b </td> </tr> 
<tr> <td> Menkalinan </td> <td> 1013 </td> <td> c </td> </tr> 
<tr> <td> Menkar </td> <td> 1014 </td> <td> d </td> </tr> 
<tr> <td> Menkent </td> <td> 1028 </td> <td> e </td> </tr> 
<tr> <td> Menkib </td> <td> 1029 </td> <td> f </td> </tr> 
<tr> <td> Merak </td> <td> 1030 </td> <td> a </td> </tr> 
<tr> <td> Merga </td> <td> 1031 </td> <td> b </td> </tr> 
<tr> <td> Merope </td> <td> 1032 </td> <td> c </td> </tr> 
<tr> <td> Mesarthim </td> <td> 1033 </td> <td> d </td> </tr> 
<tr> <td> Miaplacidus </td> <td> 1034 </td> <td> e </td> </tr> 
<tr> <td> Mimosa </td> <td> 1035 </td> <td> f </td> </tr> 
<tr> <td> Minchir </td> <td> 1036 </td> <td> a </td> </tr> 
<tr> <td> Minelava </td> <td> 1037 </td> <td> b </td> </tr> 
<tr> <td> Minkar </td> <td> 1038 </td> <td> c </td> </tr> 
<tr> <td> Mintaka </td> <td> 1039 </td> <td> d </td> </tr> 
<tr> <td> Mira </td> <td> 1040 </td> <td> e </td> </tr> 
<tr> <td> Mirach </td> <td> 1015 </td> <td> f </td> </tr> 
<tr> <td> Miram </td> <td> 1016 </td> <td> a </td> </tr> 
<tr> <td> Mirfak </td> <td> 1017 </td> <td> b </td> </tr> 
<tr> <td> Mirzam </td> <td> 1018 </td> <td> c </td> </tr> 
<tr> <td> Misam </td> <td> 1019 </td> <td> d </td> </tr> 
<tr> <td> Mizar </td> <td> 1020 </td> <td> e </td> </tr> 
<tr> <td> Mothallah </td> <td> 1021 </td> <td> f </td> </tr> 
<tr> <td> Muliphein </td> <td> 1022 </td> <td> a </td> </tr> 
<tr> <td> Muphrid </td> <td> 1023 </td> <td> b </td> </tr> 
<tr> <td> Murzim </td> <td> 1024 </td> <td> c </td> </tr> 
<tr> <td> Muscida </td> <td> 1025 </td> <td> d </td> </tr> 
<tr> <td> Muscida </td> <td> 1026 </td> <td> e </td> </tr> 
<tr> <td> Muscida </td> <td> 1027 </td> <td> f </td> </tr> 
</table> </html>
"""

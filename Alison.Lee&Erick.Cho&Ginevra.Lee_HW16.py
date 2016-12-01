# Team GEA - Ginevra Lee, Erick Cho, Alison Lee
# IntroCS2 pd8
# HW16 -- String The Loops
# 2016 - 03 - 15

# 1

def addMultPrint(a,b):
    print "the sum of " + str(a) + " and" + str(b) + " is " + \
        str((a+b)) + ", their product is " + str (a*b)          
                #add the words as strings, and convert the numbers
                #into strings with str
addMultPrint(3,6)
# answer should be "the sum of 3 and 6 is 9 their product is 18

# 2
def multHTML(a,b):
    print "<html> <body> the <i> sum </i> of " \
          + str(a) + " and " + str(b) + " is " \
          + "<b> " + str(a+b) + " </b>" + " <br>" \
          + " their <i> product </i> is <b> " + str(a*b)\
          + " </b> </body> </html>"
    
multHTML(3,6)
#should return <html> <body> the <i> sum </i> of 3 and 6 is <b> 9 </b>
#<br> their <i> product </i> is <b> 18 </b> </body> </html>
#renders as the (italics) sum of 3 and 6 is 9 (bolded)
#their (italics) product is 18 (bolded)

# 3
def sumDigits ( n ) :
    rem = n % 10
    res = 0
    while n > 0 :
        res = res + rem
        n = n / 10
        rem = n % 10
    return res

def squares(n):
    while n >= 1:  
        ans = n**2 
        return ans  
        n = n - 1

    # TABLE FORMAT
        # <table border = "1" >
        #   <tr>
        #       <td> text </td>
        #   </tr>
        # </table>

def tablefy ( n ) :
    ton = 1
    # means to n. 
    print "<html> <table border = '1'> <tr> <td> n </td> <td> n^2 </td> <td> sumDigits </td> </tr>"
    # this shouldn't be looped so it goes before the while loop
    while ton <= n :
        # it will stop when ton is equal to n, printing 11 rows (including the first row)
        print "<tr> <td> " + str( ton ) + " </td> <td> " + str( squares( ton )) + " </td> <td> " + str( sumDigits( squares( ton ))) + " </td> </tr>"
        ton += 1
    print "</table> </html>"

tablefy ( 10 )
# should print:
    # <html> <table border = '1'> <tr> <td> n </td> <td> n^2 </td> <td> sumDigits </td> </tr>
    # <tr> <td> 1 </td> <td> 1 </td> <td> 1 </td> </tr>
    # <tr> <td> 2 </td> <td> 4 </td> <td> 4 </td> </tr>
    # <tr> <td> 3 </td> <td> 9 </td> <td> 9 </td> </tr>
    # <tr> <td> 4 </td> <td> 16 </td> <td> 7 </td> </tr>
    # <tr> <td> 5 </td> <td> 25 </td> <td> 7 </td> </tr>
    # <tr> <td> 6 </td> <td> 36 </td> <td> 9 </td> </tr>
    # <tr> <td> 7 </td> <td> 49 </td> <td> 13 </td> </tr>
    # <tr> <td> 8 </td> <td> 64 </td> <td> 10 </td> </tr>
    # <tr> <td> 9 </td> <td> 81 </td> <td> 9 </td> </tr>
    # <tr> <td> 10 </td> <td> 100 </td> <td> 1 </td> </tr>
    # </table> </html>


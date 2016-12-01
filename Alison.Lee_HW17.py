# Alison Lee
# IntroCS pd8
# HW17 -- 000 000 111 (007, I see I see)
# 2016-03-17

def bondify ( name ) :
    n = 0
    # this will be the index for the name
    newname1 = ""
    while name[ n ] != " " :
        # THIS while loop will run until it reaches the space btwn the
            # first and last name. 
        newname1 += name[ n ]
        # newname1 should return the first name, letter by letter
        n += 1
    # after this while loop runs, name[ n ] should currently be " "
    n += 1
    # and now, name[ n ] will be the first letter of the last name
    newname2 = ""
    while n < len( name ) :
    # it's not like the code will run 2+ times so I figured that it wouldn't
        # be risky to have two while loops in the function
    # basically, you do the same thing, but you're forming and storing the
        # last name in a different variable
        newname2 += name[ n ]
        n += 1
    return newname2 + ", " + newname1 + " " + newname2
    # in other words, "[ Last Name ], [ First Name ] [ Last Name ]"

print bondify ( "James Bond" )
# should print "Bond, James Bond"
print bondify ( "L Lawliet" )
# should print "Lawliet, L Lawliet"

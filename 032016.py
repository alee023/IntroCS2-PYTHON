def indexOf ( s , ch ) :
    index = 0
    # so s[ index ] should return the 1st character of the string
    while ( index <= len( s )) :
        # it's unnecessary to have "while ... or s[ index ] != ch" included
        # because the "return index" at the very bottom of the function
        # will stop the while loop once it reaches the desired character
        if index + 1 > len( s ) :
            # one has to be added to index because
            # the index of the last letter will be len( s ) - 1
            # index starts counting from 0 while len starts at 1 apparently
            return -1
        elif (( s[ index ] != ch ) and ( index < len( s ))) :
            # one is added to index as long as s[ index ] doesn't return
            # the desired character yet, and as long as it is less than
            # the length of the string
            index += 1
        elif s[ index ] == ch :
            return index
        # as said above, this will stop the while loop once
        # s[ index ] returns the desired character

print indexOf ( "Hey hai" , "a" )
# this should return 5
print indexOf ( "Hey hai" , "z" )
# this should return -1
print indexOf ( "Hey hai" , "H" )
# this should return 0

# Alison Lee 
# IntroCS2 pd8 
# HW29 -- Change is for the best (labwork)
# 2016-04-08 
 
# 1. F - this function goes through the entire list so a for loop is suitable. If using 
       # a while loop, an additional variable (index, pos, etc) has to be created 
# 2. W - this function is supposed to create a list. The loop also has to stop at 
       # at some point, with the condition based on the list that it is creating. 
       # Cannot see how a for loop will accomplish this so I used a while loop. 
# 3. F - Also goes through an entire list.  
 
# 1 
def listFind ( L , q ) : 
# helper function. If L.index( w ) isn't allowed. 
    n = 0 
    for w in L : 
        if w == q : 
            return n 
        else : 
            n += 1 
    if w == L[ -1 ] and w != q : 
        n = -1 
    return n 
 
def rmNegatives( L ) : 
    for w in L : 
        if w < 0 : 
            L = L[ : listFind( L , w ) ] + L[ listFind( L , w ) + 1 : ] 
            # instead of L[ : w] + L[ w + 1 : ] (which worked for the two test  
            # cases yesterday but not today???), I used listFind from the  
            # other day. It was changed because it was finding L[ -4 ], for  
            # example,   
       # or L = L[ : L.index( w ) ] + L[ L.index( w ) + 1 : ] 
    print L  
             
# rmNegatives( [ 5 , 4 , 3 , 2 , 1 ] ) 
# [ 5 , 4 , 3 , 2 , 1 ] 
rmNegatives( [ 5 , -4 , 3 , -2 , 1 , 0 ] ) 
# [ 5 , 3 , 1 , 0 ] 
rmNegatives( [ 0 , -1 , 2 , -3 , 4 , -5 ] ) 
# [ 0 , 2 , 4 ] 
 
# 2 
def listFib( n ) : 
    fib = 0 
    # the fib number that will be added to the list 
    store = 0 
    # also the previous fib number. It's necessary because I want to change 
    # fib and prev at the same time andddd I'm not using multiple assignment 
    prev = 1 
    # prev is the previous fib number 
    L = [ ] 
    while len( L ) < n : 
    # the length of the list should be equal to n 
        L += [ fib ] 
        store = fib 
        # this will store the current (or previous depending on how 
        # you view it) fib number 
        fib += prev 
        # the new fib number is the sum of the current (or previous) 
        # and the number before that 
        prev = store 
    print L 
 
listFib( 1 ) # [ 0 ] 
listFib( 2 ) # [ 0 , 1 ] 
listFib( 3 ) # [ 0 , 1 , 1 ] 
listFib( 4 ) # [ 0 , 1 , 1 , 2 ] 
listFib( 5 ) # [ 0 , 1 , 1 , 2 , 3 ]  
listFib( 6 ) # [ 0 , 1 , 1 , 2 , 3 , 5 ] 
listFib( 7 ) # [ 0 , 1 , 1 , 2 , 3 , 5 , 8 ] 
listFib( 8 ) # [ 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 ] 
 
# 3 
def sentify( L ) : 
    s = "" 
    for w in L : 
        s += w + " " 
        # the word and a space is added to the new string each time 
    print s 
 
sentify( [ "this" , "is" , "how" , "we" , "do" ] ) 
# "this is how you do "     

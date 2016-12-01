# Alison Lee
# IntroCS2 pd8
# HW28 -- For vs. While
# 2016-04-07

# 1. F - this function goes through the entire list so a for loop is suitable. If using
       # a while loop, an additional variable (index, pos, etc) has to be created
# 2. W - this function is supposed to create a list. The loop also has to stop at
       # at some point, with the condition based on the list that it is creating.
       # Cannot see how a for loop will accomplish this so I used a while loop.
# 3.

# 1
def rmNegatives( L ) :
    for w in L:
        if w < 0:
            L.remove( w )
            # a function that removes numbers less than 0
    print L  

""" def rmNegatives( L ) :
    for w in L :
        if w <= 0 :
            L = L[ : w ] + L[ w + 1 : ]
            # keeps the part before the negative and the part of the list after the
            # negative. It's L[ w + 1 : ] (rather than L[ w : ] because it will not
            # include the negative num
    print L """
            
rmNegatives( [ 5 , 4 , 3 , 2 , 1 ] )
# [ 5 , 4 , 3 , 2 , 1 ]
rmNegatives( [ 5 , -4 , 3 , -2 , 1 , 0 ] )
# [ 5 , 3 , 1 ]

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
    return L

print listFib( 1 ) # [ 0 ]
print listFib( 2 ) # [ 0 , 1 ]
print listFib( 3 ) # [ 0 , 1 , 1 ]
print listFib( 4 ) # [ 0 , 1 , 1 , 2 ]
print listFib( 5 ) # [ 0 , 1 , 1 , 2 , 3 ] 
print listFib( 6 ) # [ 0 , 1 , 1 , 2 , 3 , 5 ]
print listFib( 7 ) # [ 0 , 1 , 1 , 2 , 3 , 5 , 8 ]
print listFib( 8 ) # [ 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 ]

# 3
def sentify( L ) :
    s = ""
    for w in L :
        s += w + " "
        # the word and a space is added to the new string each time
    print s

sentify( [ "this" , "is" , "how" , "we" , "do" ] )
# "this is how you do "      

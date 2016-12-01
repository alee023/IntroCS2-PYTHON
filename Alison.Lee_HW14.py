#Alison Lee
#IntroCS pd8
#HW14 -- Repetition Two Ways
#2016-03-12

#1
def factR ( n ) :
    if n <= 1 :
        return 1
        # here, recursion is used, and n <= 1 is the base case.
        # n * ( n - 1 ) * ( n - 2 ) ...
    else :
        return n * factR ( n - 1 )


#2
def factW ( n ) :
    if n <= 1 :
        return 1
    # anything other than 1 should return 1
    num = n - 1
    # here, I created a local variable called num and it is the next number
    #    to multiply to n, which is why it is already 1 less than n
    result = n
    while num > 1 :
    #only runs when n > 1
        result = result * num
        # the equivalent of n * ( n - 1 )
        num = num - 1
        # will set num to n - 2 and so on... (n - 3, n - 4, ...)
    return result


# Team - Alison Lee & Erick Cho
# IntroCS2 pd8
# HW27 -- Back in the [Co]Driver's Seat, Looping_FTW
# 2016-04-07

# 1
def listSum( L ) :
    n = 0
    for i in L :
        n += i
        # the value of i (the numbers in the list) get added onto n, which is
        # the sum of the previous values of i
    print n

listSum( [ 0 , 1 , 2 , 3 ] ) # 6

# 2
def minVal( L ) :
    n = L[ 0 ]
    for w in L :
        if n > w :
        # whenever a number is lower than the previous one, n is
        # redefined to be the one of lower value
            n = w
    print n

minVal ( [ 3 ] ) # 3
minVal ( [ 5 , 4 , 3 , 2 , 1 ] ) # 1

#3
def listFind ( L , q ) :
    n = 0
    for w in L :
        if w == q :
            return n
            # stops the loop when q is encountered 
        else :
            n += 1
            # else moving on to the next number. 1 is added to n
    if w == L[ -1 ] and w != q :
    # didn't think that it had to be looped. At this point, the for loop
    # has gone through the entire list and q has either been found or hasn't
    # been found. If it hasn't been found, then n = -1
        n = -1
    return n

print listFind([5,4,3,2,1,],6) # -1
print listFind([5,4,'cat','dog','cat'],'cat') # 2
print listFind( [ 1 , 2 , 3 , 4 , 5 ] , 3 ) # 2

#4 
def minPos(L):
    # same as minVal but there is a counter n
    n=0
    Min=L[0]
    for w in L:
        if w<Min:
            w=Min
            n+=1
    return n

print minPos([3]) # 0
print minPos([5,4,3,2,1]) # 4

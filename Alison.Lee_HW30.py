"""
Team maeT - Darren Liang, Alison Lee
IntroCS2 pd8
HW30 - Removal Three Ways
2016 - 04 - 12
"""

"""
pop()
-Removes and returns the element at the index value of the input from the list.
-If there is no input, it removes and returns the last element.
-Error if index is out of range.

remove()
-Removes the input value from the list.
-Error if the input value is not found in the list.

del
-Removes an item at the index value (does not return).
-Can remove "slices", or a bunch of elements at the same time.
-Can delete variables

Our team used L.remove() instead because it can take and removes the value,
making it much more convenient than the other library functions.
The code is the same no matter which one we used, however, because we removed the
negative number at an index value. 

"""

"""def rmNegPop(L):
    i = 0
    while i < len(L):
        if L[i] < 0:
            L.pop(i)
        else:
            i += 1

print rmNegPop([-1,-2,0,4,-5])"""

def rmNegRemove(L):
    i = 0
    while i < len(L):
        if L[i] < 0:
            L.remove(L[i])
        else:
            i += 1

print rmNegRemove([-1,2,-5,4,-5])

"""def rmNegDel( L ) :
    i = 0
    while i < len( L ) :
        if L[ i ] < 0 :
            del L[ i ]
        else :
            i += 1

rmNegRemove([ 1 , -2 , -3 , 4 , -5 ])"""

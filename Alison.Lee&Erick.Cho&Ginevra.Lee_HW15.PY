# Team Erick Cho, Alison Lee, Ginevra Lee
# IntroCS pd8
# HW15 -- Loopy
# 2016-03-14

# 1
def sumDigits ( n ) :
    rem = n % 10
    res = 0
        # 2 local variables were created. rem stands for remainder and
        # res for result
    while n > 0 :
        res = res + rem
        # so far, the sum is the last digit 
        n = n / 10
        # the last digit is eliminated
        rem = n % 10
        # this will set rem to the last digit of the new n value
    return res

# sumDigits ( 234 ) should return 9
# sumDigits ( 22 ) should return 4
# sumDigits ( 3 ) should return 3
# sumDigits ( 6666 ) should return 24

# 2
def squares(n):
    while n >= 1:  #base case is 1
        ans = n**2 #answer
        print n, ans  #makes the function print the numbers and its squares
        n = n - 1  #set new number, goes through the loop again

#squares(3) #answer should be 3 9; 2 4; 1 1
#squares(5) #answer should be 5 25; 4 16; 3 9; 2 4; 1 1
#squares(1) #answer should be 1 1

# 3
def sumPerfSquares ( n ) :
    result = 0
    while n >= 1 :
        ans = n ** 2
        result = result + ans
        # sets result to ans at first, and then adds the next ans to result
        # until the while loop stops running
        n = n - 1
    return result
    # based off #2

# sumPerfSquares ( 3 ) should return 14
# sumPerfSquares ( 1 ) should return 1
# sumPerfSquares ( 2 ) should return 5
# sumPerfSquares ( 5 ) should return 55
    


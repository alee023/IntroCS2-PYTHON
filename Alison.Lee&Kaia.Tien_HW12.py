#Team Name: The Dynamic Duo
#Kaia Tien and Alison Lee
#IntroCS2 pd 8
#HW#12--PassJudgement
#2016-03-10



#1
def pythTriple(a,b,c):
    if a==0 or b==0 or c==0:
        return False
    if (a**2) + (b**2) == c**2:
        return True   
    else:
        return False
    #return (( a ** 2 ) + ( b ** 2 ) == ( c ** 2 ))

#pythTriple(0,0,0)
#Answer should be False

#pythTriple(3,4,5)
#Answer should be True

#pythTriple(3,4,6)
#Answer should be False

#pythTriple(32,255,257)
#Answer should be True

#2
def gradeConv (g):
    if g >= 90 and g <= 100:
        return "A"
    if g >= 80 and g <= 89:
        return "B"
    if g >= 70 and g <= 79:
        return "C"
    if g >= 65 and g <= 69:
        return "D"
    else:
        return "F"

# gradeConv(95) should return A
# gradeConv(80) should return B
# gradeConv(67) should return D
# gradeConv(5) should return F

#3
def passJudgement ( letterGrade ):
    if letterGrade == "A" or letterGrade == "B":
        return "Congratulations! You did great!"
    if letterGrade == "C":
        return "Work a little harder"
    if letterGrade == "D":
        return "You need to step up your game"
    else:
        return "Seek help"

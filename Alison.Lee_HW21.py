# Team Number Juan - Tahseen Chowdhury, Erick Cho, Oskar Mai, Alison Lee
# IntroCS2 pd8
# HW21 -- Cereal Grade Encryption
# 2016-03-26

#1
def rot13 ( ch , beg ) :
    # beg for beginning 
    ascii = ord( ch )
    if abs( ascii - beg ) >= 13 :
        return chr( ascii - 13 )
    else :
        return chr( ascii + 13 )
    # letters closer to 'z'/'Z' have to have 13 subtracted from them and ones
    # closer to 'a'/'A' has 
# my helper function - basically the converting function

def rot13Chr ( ch ) :
    if ord( ch ) >= 65 and ord( ch ) <= 90 :
        beg = 65
    else :
        beg = 97
    return rot13 ( ch , beg )

print rot13Chr("i")
# should print v
print rot13Chr("l")
# should print y
    
# 2
def printEmAll():
    counter = 65
    while counter != 123:
        if counter == 91:
            counter = 97
            # will jump from chr( "Z" ) to chr( "a" )
        print chr(counter) + " <-> " + rot13Chr(chr(counter))
        counter += 1

printEmAll()
# should print: 
# A <-> N
# B <-> O
# C <-> P
# D <-> Q
# E <-> R
# F <-> S
# G <-> T
# H <-> U
# I <-> V
# J <-> W
# K <-> X
# L <-> Y
# M <-> Z
# N <-> A
# O <-> B
# P <-> C
# Q <-> D
# R <-> E
# S <-> F
# T <-> G
# U <-> H
# V <-> I
# W <-> J
# X <-> K
# Y <-> L
# Z <-> M
# a <-> n
# b <-> o
# c <-> p
# d <-> q
# e <-> r
# f <-> s
# g <-> t
# h <-> u
# i <-> v
# j <-> w
# k <-> x
# l <-> y
# m <-> z
# n <-> a
# o <-> b
# p <-> c
# q <-> d
# r <-> e
# s <-> f
# t <-> g
# u <-> h
# v <-> i
# w <-> j
# x <-> k
# y <-> l
# z <-> m

# 3
def rot13Wrd ( word ) :
    index = 0
    newWord = ""
    while index < len( word ) :
        # will convert a letter at a time. It stops running once it
        # reaches the end of the word
        newWord += rot13Chr( word[ index ] )
        index += 1
    return newWord

print rot13Wrd( "TEAM" )
# should print GRNZ
print rot13Wrd( "number" )
# should print ahzore
print rot13Wrd( "Juan" )
# should print Whna



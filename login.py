#!/usr/bin/python
print "Content-Type: text/html\n\n"
print ""
print "<!DOCTYPE html> <html>"
import cgi
import cgitb
# cgitb.enable()

def read(txt):
    theFile = open(txt,'r')
    L = theFile.readlines()
    theFile.close
    return L

def usr():
    d = cgi.FieldStorage()
    username = d['user'].value
    return username

def pwd():
    d = cgi.FieldStorage()
    password = d['pass'].value
    return password

home = "<a href='home.html'> here </a>"
back = "<a href='login.html'> Back </a>"

u = usr()
p = pwd()
d = open('users.txt','r')

names = d.readlines()

def infoL():
    accounts = []
    for sublist in names:
        q = sublist.strip()
        accounts.append(q)
    return accounts

accounts = infoL()

def isUser():
    if str(u + " " + p) in accounts:
        print "Logged in <br>\
Click " + home + " to continue"
    else:
        print "Wrong info. Try again. <br>\
" + back + ""
    return ""

print isUser()
print "</html>"


    

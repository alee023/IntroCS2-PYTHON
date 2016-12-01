#!/usr/bin/python
print "Content-Type: text/html\n\n"
print ""
print "<!DOCTYPE html>"
print "<html>"
import cgi
import cgitb
cgitb.enable()

def write(txt, data):
    theFile = open(txt,"a")
    theFile.write(data)
    theFile.write("\n")
    return txt
    
def getUser():
    d = cgi.FieldStorage()
    username = d['user'].value
    return username

def getPass():
    d = cgi.FieldStorage()
    password = d['pass'].value
    return password

login = "<a href='login.html'> here </a>"
back = "<a href='create.html'> Back </a>"

u = getUser()
p = getPass()
d = open('users.txt','r')

names = d.readlines()

def namesL():
    users = []
    accounts = []
    for sublist in names:
        q = sublist.strip()
        accounts.append(q)        
    for combo in accounts:
        space = combo.find(' ')
        users.append(combo[:space])
    return users

users = namesL()

if u in users:
    print "That username is taken. <br>" + back
else:
    users.append(u)
    data = u + " " + p
    write('users.txt',data)
    print "Congratulations!!! You've made an account. <br>\
Log In " + login

print "</html>"



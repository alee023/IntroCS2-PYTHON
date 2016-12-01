#!/usr/bin/python
# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========

"""
Team Blue - Alison Lee, Henry Zheng
IntroCS2 pd8
HW#57 -- Formal Textification
2016-05-31
"""

import cgi
import cgitb
# cgitb.enable()  #diag info --- comment out once full functionality achieved
query = cgi.FieldStorage()

# ~~~~~~~~~~~~~~~ support functions ~~~~~~~~~~~~~~~
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d

def rot13Chr( ch ) :
    if ch.upper() == ch :
        offset = ord( 'A' )  #65
    else :
        offset = ord( 'a' )  #97
    if (( ch == " " ) or ( ord( ch ) < 65 ) \
        or (( 90 < ord( ch ) < 97 )) \
        or ( ord( ch ) > 122 )) :
        result = ch
    else :
        result = chr(( ord( ch ) + 13 - offset ) % 26  + offset )
    return result

def rot13( value ) :
    newPhrase = ""
    for n in value :
        newPhrase += rot13Chr( n )
    return newPhrase

def reverse( value ) :
    return value[::-1]

def areaCGI():
    keys = query.keys()
    text = query["text1"].value
    type1 = query["type1"].value
    if type1 == "rot13":
        text = rot13(text)
    if type1 == "reverse":
        text = reverse(text)
    if "bold" in keys:
        text = "<b>" + text + "</b>"
    if "italics" in keys:
        text = "<i>" + text + "</i>"
    if "underline" in keys:
        text = "<u>" + text + "</u>"
    if "allofthem" in keys:
        text = "<b><i><u>" + text + "</b></i></u>"
    return text

# ========= CONTENT-TYPE LINE REQUIRED. ===========
# ======= Must be beginning of HTML string ======== 
htmlStr = "Content-Type: text/html\n\n" #NOTE there are 2 '\n's !!! 
htmlStr += "<html><head><title> Formal Textification </title></head></html>\n"
htmlStr += "<body>"

# ~~~~~~~~~~~~~ HTML-generating code ~~~~~~~~~~~~~~
htmlStr += "<h3>Formal Textification</h3>"
htmlStr += "<h4>Data Input:</h4>"
htmlStr += str( FStoD() )
htmlStr += "<h4>Data Output:</h4>"
htmlStr += areaCGI()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

htmlStr += "</body></html>"


print htmlStr

#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

# Alison Lee
# IntroCS2 pd8
# HW52 -- GET Started Simply
# 2016-05-23

import os
d = os.environ

print "Query String" + d[ "QUERY_STRING" ]

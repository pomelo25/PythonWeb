#!python

import cgi

form = cgi.FieldStorage()
title = form["title"].value
description = form["decsription"].value

open_file = open('data/' + title, 'w')
open_file.write(description)

# Redirection
print("Location: index.py?id="+title)
print()

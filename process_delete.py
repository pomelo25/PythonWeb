#!python

import cgi, os

form = cgi.FieldStorate()
pageId = form["pageId"].value

os.remove('data/' + pageId)

print("Location: index.py")
print()

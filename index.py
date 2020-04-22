#!python
print("Content-Type: text/html")
print()

import cgi, os

files = os.listdir('data')
listStr = ''

# 리스트 목록
for item in files:
  listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

# 제목, 내용
form = cgi.FieldStorage()

if 'id' in form:
  pageId = form["id"].value
  description = open('data/' + pageId, 'r').read()
  update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
else:
  pageId = 'Welcome'
  description = 'Hello Web'
  update_link = ''

print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset=utf-8>
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    # 리스트 목록
    {listStr}
  </ol>
  <a href="create.py">create</a>
  {update_link}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr, update_link=update_link))

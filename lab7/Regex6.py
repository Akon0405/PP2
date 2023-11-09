import re
file=open('row.txt', 'r', encoding="utf-8")
text = file.read()
result=re.sub("[ ,.]",':', text)

print(result)
file.close()
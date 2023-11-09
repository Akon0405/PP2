import re
file=open('row.txt', 'r', encoding="utf-8")
text = file.read()
x=re.findall(r'[A-Z][a-z]+', text)

if x:
    print(x)
    print("Found")
else:
    print("Not Found")
file.close()
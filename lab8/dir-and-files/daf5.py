color = ["column", "word", "number"]
with open('row.txt', "w") as fr:
        for i in color:
                fr.write("%s\n" % i)
content = open('row.txt')
print(content.read())
import os
fileToWrite = 'theReply.txt'
lol = input("is anime based? ")

if lol == "yes":
    output ="go outside"
elif lol == "i love roblos":
    output = "YOOOOOOOOOOOOO SAME!!!!"
elif lol == "no":
    output ="based"
else:
    output ="fair enough"
# print(output)

fh = open(fileToWrite, 'w')
fh.write(output)

os.startfile(fileToWrite)
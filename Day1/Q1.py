#valid email address
import re
f = open("emails.txt",'r')
rex = re.compile('@')
while True:
    str1 = f.readline()
    if str1:
        if rex.search(str1):
            print"valid"
        else:
            print"invalid"
        
    else:
        break

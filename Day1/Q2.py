import re
f = open("urls.txt",'r')
rex = re.compile('www.')
rex2 = re.compile('.com')
while True:
    str1 = f.readline()
    if str1:
        if rex.search(str1) and rex2.search(str1):
            print"VALID"
        else:
            print"INVALID"
    else:
        break
        

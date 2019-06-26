"""1.	Define a list as below
List1 = [47,11,42,102,13]
	Find maximum number by using reduce() function
"""
#find max using reduce
List1 = [47,11,42,102,13]

def max(x,y) :
    if x>y :
        return x
    else : return y
print reduce(max,List1)        

"""
6. Let’s say I give you a list saved in a variable:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list b 
that has only the even elements of this list in it. (Use filter and lambda)

"""
b=[]
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b =( filter(lambda x : x%2 == 0 , a))
print b


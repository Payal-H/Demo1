"""
2.	Given temperatures in a list like-
Celsius = [39.2, 36.5, 37.3, 37.8]
a)	Convert all these temperature values into Fahrenheit and store in a
target list – Fahrenheit =[]
      Use map and lambda. Hint : formula - (float(9)/5)*x + 32

b) Convert above Fahrenheit list into Celsius list.
     Use map and lambda. Hint : formula - (float(5)/9)*(x-32), 
"""
c=[]
Celsius = [39.2, 36.5, 37.3, 37.8]
target_list_Fahrenheit =[]
target_list_Fahrenheit= map(lambda x :(float(9)/5)*x + 32 ,Celsius)
print "Temperature in Celsius : ",Celsius
print "Temperature in Fahrenhit ",target_list_Fahrenheit
c = map(lambda x :(float(5)/9)*(x-32),target_list_Fahrenheit)
print " ",c
 

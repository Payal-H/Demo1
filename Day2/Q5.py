
"""
Create Employee class.
Define instance variables Name and salaray.
Accept Name and Salary for every person from keyboard (raw_input() function
to be used)Also write instance method “displayEmployee()
to display all employee details (Name and Salary)
"""
class Employee :
    empCount = 0

    def __init__(self,name,sal,count):
        self.name=name
        self.sal=sal
        self.n=count
        print" constructor"
    

    def displayEmployee(self):
         print "Name :",self.name
         print "Salary :",self.sal
         print self.n
print"*****************************************"
#ob[]
emp = {}
str1= []
sal= []
n=1
#n = raw_input("Enter the Number Of ")

while 1 :
    name=raw_input("Enter the name:  ")
    sal1 = raw_input("Enter the Salary: ")

    if name:
       str1.append(name)
       sal.append(sal1)
       n += 1

    else:
        break
ob1 = Employee(str1,sal,n)
#ob1.displayCount()
ob1.displayEmployee()

"""

     #   emp[list1[0]]=int(list1[1])

        
    #else :
    str1.append())
    X
    
    
    
    #emp[str1]=int(sal)
    
    #ob1 = Employee(str1,sal)
    #ob1.displayCount()
    #ob1.displayEmployee()
"""

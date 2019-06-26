"""3.	Create Employee class.
Maintain class level variable “empCount”  and write function “displayCount()”to 
display the total empCount. 
Define instance variables Name and salaray.
Also write instance method “displayEmployee() to displa0y all
employee details (Name and Salary)
"""

class Employee :
    empCount = 0

    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
        Employee.empCount += 1

    def displayCount(self):
        print "Total Count Of Employees : ",Employee.empCount

    def displayEmployee(self):
         print "Name :",self.name
         print "Salary :",self.sal

print"*****************************************"

ob1 =Employee("payal",45000)
ob1.displayCount()
ob1.displayEmployee()

"""
4.	Create BankAccount class
Specify initial amount in Bank account as 50000
Write functionality for 	showBalance()
			Deposit(amount)
			WithDrawl(amount)
Error to be handled if Withdraw amount is greater that available balance.	

"""
class MyError(Exception):   #inheritance, superclass is Exception, MyError is subclass
    
    pass
 


class BankAccount :
    initial_amount = 50000
    updated_amt = 50000
    def __init__(self,x=1):
        print "1"
        
    def showBalance(self):
        print updated_amt
                
    def Deposit(self,amount):
        updated_amt= self.updated_amt+amount
        print updated_amt
        
    def WithDrawl(self, amount):
        
        
        updated_amt= self.updated_amt-amount
       
        try:
            
            if amount > updated_amt :
    
                raise MyError("Some information about what went wrong")
            else :
                
                print updated_amt
        except MyError as error:
            print("Situation:", error)
        
 

print"*******************************************"

ob1 = BankAccount()



while (1):
    print "\t1.Deposite\n\t2.Withdraw\n\t3.Show Balance\n\t4.Exit"
    op = input("Enter option  : ")
    if op=="":break

    else :
    
        if op==1:
            amount = input("Enter Amount to deposite ")
            ob1.Deposit(amount)
        
        elif op==2:
            amount = input("Enter Amount to withdraw ")

            ob1.WithDrawl(amount)
            
        elif op==3:
            ob1.showBalance()
               
    

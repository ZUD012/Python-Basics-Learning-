# Create Coount class with 2 Attributes - Balance & account no.
#Create methods for debit , credit & printing the balance 

class Account:
    def __init__ (self , bal , acc):
        self.balance = bal 
        self.acc_no  = acc
        
    def debit(self , amount):
      self.balance -=amount
      print("Rs ",amount," was debited from your account")

    def credit(self , amount):
      self.balance +=amount
      print("Rs ",amount," was credited from your account")
    
    def get_Balance(self):
       return self.balance
accont1 = Account(1000 , 12345)


accont1.debit(300)
accont1.credit(50000)
print(accont1.get_Balance())


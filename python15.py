# Understanding del Keyword -->

#class Student:
 #   def __init__(self , name ):
#     self.name = name
    
#s1 = Student("Parth")
#print(s1.name)
#del s1.name
#print(s1.name)

# Understanding how to create  private members and functions -->

class Account:
   def __init__ (self , acc_no , acc_pass):
      self.acc_no = acc_no
      self.__acc_pass = acc_pass

   def reset_pass(self):
      print(self.__acc_pass)

acc1 = Account("123456" , "abcde")

print(acc1.acc_no)
print(acc1.reset_pass())
# print(acc1.__acc_pass) --> Will Show Error . 


# understanding Concept of Inheritance
class car :
   colour = "Black"
   @staticmethod
   def start():
      print("Car Started")
   
   @staticmethod
   def stop():
       print("Car stopped. ")

class toyota_Car(car):      # Single level Inheritance -->
  def __init__(self , brand):
     self.brand = brand
     
class Fortuner(toyota_Car): # Multilevel Inheritance -->
   def __init__(self , type):
      self.type = type

car1 = Fortuner("diesel")
car1.start()

class A :
   varA = "Welcome to class A"
class B :
   varB = "welcome to class B"
class C(A , B):
   varC = "Welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)
   

class car :
   colour = "Black"
   def __init__(self , type):
      self.type = type
   @staticmethod
   def start():
      print("Car Started")
   
   @staticmethod
   def stop():
       print("Car stopped. ")

class toyota_Car(car):      # Single level Inheritance -->
  def __init__(self , name , type) :
     self.name = name
     super().__init__(type) #type class of Parent class .
     super().start()
     

car1 = toyota_Car("pirus" , "Electric")
print(car1.type)
     

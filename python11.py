# Object oriented programming -->

class student :
    def __init__ (self , ): # default constructor . 
        pass
    college_name  = "ABES COLLEGE"
    def __init__ (self , fullname , marks): # Parameterised Constructor .
        self.name = fullname
        self.marks = marks
        print("Adding New stuent in Database --> ")
    @staticmethod
    def hello():
        print("Hello" )


  

s1 = student("Karan" , 78)
print(s1.name)
print(student.college_name)
       #OR
print(s1.college_name)
s1.hello()

#class Car :
#    colour = "Black"
#    brand  = "BMW"
#
#car1 = Car()
#print(car1.colour)
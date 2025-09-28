class person:
    name = "anonymous"
    
    #def ChangeName(self , name):
        # person.name = name
              #OR
        #self.__class__.name = "Rahul"
    @classmethod
    def ChangeName(cls , name):
        cls.name = name


p1 = person()
p1.ChangeName("Rahul Singh")
print(p1.name)
print(person.name)      

class Student :
    def __init__(self , phy , chem , math):
        self.phy = phy
        self.chem = chem
        self.math = math
       
    
    #def calculate_percent(self):
    #    self.percentage = str((self.phy+self.chem+self.math) /3) + " %"

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math) /3) + " %"
    
stu1 = Student(98,99,97)
print(stu1.percentage)

stu1.phy = 86    
print(stu1.percentage)              
print(stu1.phy)


    
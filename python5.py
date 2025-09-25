# Dictionaries in Python -->

student ={"Ramesh" : 2 ,
          "Kapil" : 32 ,
          "Subject" :{
           "Phy" : 7 ,
           "Maths" : 8
 }} 
newone = {"kamal":20}

print(student)
print(student["Ramesh"])

print(student.keys()) # Returns all key values .

print(len(student)) # Returns the length of the dictionary .

print(student.values()) #return all the values of keys in dictionary .

print(student.items()) # returns all keys and pair values inside a dictionary .

print(student.get("Maths")) # Returns the value of Key Maths .

student.update(newone) # Adds newone to student dictionary .
print(student)
# File handling (I/O) in python -->

import os 

# Reading in file -->

f = open("D:\\Python Basics Coding\\demo.txt" , "rt") #Opened a file ->
data = f.read(4)
data1 = f.readline()
print(data)
print(data1)
print(type(data))
f.close()


# Writing inside a file -->

f = open("D:\\Python Basics Coding\\demo.txt" , "w") #Opened a file ->
f.write("           Dreams are meant to be achieved think delusional but make sure they become the reality .") 


f = open("Visionboard.txt" , "w")
f.write("BMW m5 will be soon in my house and i am going for a trip to mussorie in it --> ")


# Appending inside a file -->

f = open("D:\\Python Basics Coding\\demo.txt" , "a") #Opened a file ->
f.write("\nParth is going to create one of the best startups which is distruptive .") 

# Combining of modes(r+) --> 
f = open("demo.txt" , "r+" ) # r+ mode is used to overwrite at beggning of the file >--<
f.write("Start-->")
print(f.read())
f.close()

# Combining of modes(w+) -->
f = open("Visionboard.txt" , "w+" ) # w+ mode >--<
f.write("Start-->")
print(f.read())
f.close()


# Combining of modes(a+) -->
f = open("Visionboard.txt" , "a+" ) # w+ mode >--<
f.write("Start-->")
print(f.read())
f.close()


with open("Visionboard.txt" , "r") as s : # Automatically the file gets closed when the programme is ended >--<
    data = s.read() 
    print(data)

os.remove("Visionboard.txt")
   




              
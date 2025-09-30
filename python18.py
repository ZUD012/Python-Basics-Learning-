# How to create NumPy Array with Random Numbers -->

import numpy as np 

# Rand() Function --> 

var = np.random.rand(4)
print(var)

var1 = np.random.rand(2,5) # With 2 rows and 5 coloumns -->
print(var1)

print()
print()

#Randn() function

var2 = np.random.randn(5)
print(var2)

print()
print()

#Randf() function

var3 = np.random.ranf(4)
print(var3)

print()
print()

# Randint() Function

var4 = np.random.randint(1,50,5)
print(var4)

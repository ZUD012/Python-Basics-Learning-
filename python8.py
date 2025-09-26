# Understanding functions and recursion in python -->

def sum(a,b) :   #understanding functions in python .
    return a+b 

def finf_fact(a): # understanding recursion in python .
    if a < 1:
       return
    print(a) 
    return finf_fact(a-1)

a = 20 
b = 665
print(sum(a,b))

finf_fact(7) 
# Understanding  -->  for loop , While loop , continue , break , pass statements .

print("Understanding while loop --> ")
print()
i = 1 ; 
while i<=10 :
    print(i)
    i+=1

print()
print()

print("Using for loop to print elements inside an array --> ")
print()
arr =[1,2,3,4,5,6]
for i in arr :
    print(i) 

print()
print()

print("Understanding continue statements --> ")
print()
j = 1 ; 
while j<=10 :
    if j==3 :
        j+=1
        continue
    else :
     print(j)
     j+=1

print()
print()

print("Understanding Break statements --> ")
print()
arr =[1,2,3,4,5,6]
for i in arr :
    if i==5 :
        print(i)
        break
    else:
        print("Processing")
  



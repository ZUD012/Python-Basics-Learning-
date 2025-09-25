# Sets -->

sets = {1,5,7,"naman" , "Kapil" , "ZUDO"}
set2 = {1,5,7,8,9,33}
print(sets)

sets.add(9)  # Adding an element in set .
print(sets)

sets.remove(5) # Removing apaticular element from the set .
print(sets)

sets.pop()
print(sets) # Remove Random element from set . 

print(sets.union(set2)) # Adding two sets .


print(sets.intersection(set2)) # Taking Common elements from two sets .


sets.clear() # returning a empty set . 
print(sets)
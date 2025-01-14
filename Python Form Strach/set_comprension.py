#sets are used to store multiple items in a single variable.
#sets are unordered
#sets are unchangable
#sets are unindexed
#sets do not allow duplicate values

set_var = {1,2,3,4,5}  #this is a set

print(set_var)

print(len(set_var)) #It will return the length of the set

print(type(set_var)) #It will return the type of the set

set_var = set((1,2,3))#this is another method to create the set

print(set_var)

#accessing the elements of the set

for i in set_var:#it will print the elements of set
    print(i)

set_var.add(4) #It will add the element to the set

print(set_var)

set_var2 = {5,6,7,8,9} 

set_var.update(set_var2) #It will update the set with the given set or it can be add any iterable object like list,tuples,dictonaries

print(set_var)

set_var.remove(5) #It will remove the specified element from the set if the element is not present in the set then it will raise the error

print(set_var)

set_var.discard(4) #It will remove the specified element from the set if the element is not present in the set then it will not raise the error

print(set_var)

set_var.pop() #It will remove the element from the set randomly

print(set_var)

set_var.clear() #It will clear the set

print(set_var)

set_var = {1,2,3,4,5}

del set_var #It will delete the set

print("Set is deleted")
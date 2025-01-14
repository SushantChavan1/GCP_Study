#list is data structure in python that can hold multiple values
#list is mutable
#list is ordered
#list is iterable   
#list is dynamic    
#list is heterogenous
form collections import dqueue

list = [1,2,3,"Sushant"]
print(list)
list.append(4)#It will append the element at the end of list

list.insert(4,5)#It will insert the element at the given index

list.remove(5)#It will remove the element from the list

list.pop(3)#It will remove the element from the list at the given index

list.clear()#It will clear the list

print(list)

#Some optional functions

list.count(1)#It will count the number of occurence of the element in the list

list.sort()#It will sort the list

list.reverse()#It will reverse the list

print(list.copy())#It will copy the list

list.extend([1,2,3,4])#It will extend the list with the given list output will be [1,2,3,4,1,2,3,4]

#list as a stack

stack = [1,2,3,4,5]

stack.append(6)#It will append the element at the end of the list

stack.pop()#It will remove the element from the end of the list

print(stack)


#list as a queue 

queue = dqueue([1,2,3,4,5])#It will create a queue

queue.append(6)#It will append the element at the end of the queue

queue.popleft()#It will remove the element from the left of the queue

print(queue)


#List comprehension

for i in range(10):
    print(i)        


#Nested list 

list = [[1,2,3,4],[5,6,7,8]] # This is a nested list like 2D array

for i in list:  #It will print the list in matrix format
    for j in i:
        print(j)
    print("\n")






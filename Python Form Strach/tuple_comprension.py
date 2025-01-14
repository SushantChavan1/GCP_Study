#tuple is immutable
#tuple can allow the duplicate values
#tuple is ordered
#tuple is iterable
#tuple is heterogenous

tp = tuple(1,2,3)#It will create the tuple

tp = (1,2,3,4,5,6,7,8,9,10) #this is a tuple elements enclosed in ()

print(tp)   

tp = 1,2,3,4 #this is another way of defining tuple elements

print(tp)

print(tp[0]) #It will print the element at the given index

print(tp[1:3]) #It will print the elements from the given index to the given index the : is working like the string sclicing

tp = ([1,2,3],[5,6,7]) # the tuple can contain the list

#methods of tuple

print(tp.count(1)) #It will count the number of occurence of the element in the tuple

print(len(tp)) #It will return the length of the tuple


a, b, c = (1,2,3) #It will assign the values to the variables

print(a,b,c)

#tuple comprehension
#tuple printing the elements from 1 to 10
for i in tp :
    print(i)



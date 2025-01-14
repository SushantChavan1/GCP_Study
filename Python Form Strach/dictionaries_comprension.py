#dictionaries are used to store data values in key:value pairs.
#dictionary is mutable
#dictionary is unordered
#dictionary is changable
#In dictionary the values are may be any iterable object

dict1 = {
    1 : "Sushant",
    2 : "Rohan",
    3 : "Vinayak",
    4 : "Shivtej",
    5 : "Vaibhav"
} 

print(dict1)#It will print the dictionary

print(dict1[1])#It will print the value of the key

print(len(dict1))#It will return the length of the dictionary

print(type(dict1))#It will return the type 



var = dict1[3];#It will return the value of the key it act as like a get() method

print(var) 

var = dict1.keys()#It will return the keys of the dictionary

print(var)

var = dict1.values()#It will return the values of the dictionary

print(var)

dict1[5] = "Sahaji" #It will update the value of specified key

print(dict1)

var = dict1.items()#It will return the items of the dictionary as tuples in a list

print(var)

dict1.update({5 : "Saurabh"}) #It will update the dictionary

print(dict1)

dict1.pop(5) #It will remove the specified key from the dictionary

print(dict1)

dict1.popitem() #It will remove the last key from the dictionary

print(dict1)

del dict1[1] #It will delete the specified key from the dictionary

print(dict1)

for i in dict1: #It will print the keys of the dictionary
    print(i)

del dict1 #It will delete the dictionary


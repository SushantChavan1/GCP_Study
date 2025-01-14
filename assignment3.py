
st = input("Enter the string")
print(type(st))
if(type(st) == 'str'):
    if(st == st[::-1]):
        print("String is palindrom")
    else:
        print("String is not palindrom")
else:
    print("Enter only string")

def prime():
    try:
        num = int(input("Enter the number ::"))
        cnt = 0

        #Here I check the number is divisible by only the number and 1
        for i in range(1,num+1):
            if(num % i == 0):
                cnt += 1
    
        #the cnt is 2 then the number is only divisible by 1 and itself if it is true "the number "
        if(cnt == 2):
            print(num ," is prime")
        else:
            print(num , "is not prime")
    except:
        print("Only the intger is accepetable")
        prime()
prime()
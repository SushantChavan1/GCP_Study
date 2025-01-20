
def addMarrix():
    size1 = int(input("Enetr the size of mastrix m1"))
    size2 = int(input("Enetr the size of mastrix m2"))
    if(size1 == size2):
        pass
    else:
        print("the matrix is should be an square matrix")
        addMarrix()
    m1 = []
    m2 = []
    ans = []
    print("Enter the elements of matrix")

    for i in range(0 , size1):
        li = []
        for j in range (0 , size1):
            
            num  = int(input())
            li.append(num)
        m1.append(li)
    
    print("Enter the second matix element")
    for i in range(0 , size1):
        li = []
        for j in range (0 , size1):
            num  = int(input())
            li.append(num)
        m2.append(li)
    print("The addition of the matrix is ")
    for i in range (0 , size1):
        li = []
        for j in range(0 , size1):
            n = m1[i][j] + m2[i][j]
            li.append(n)
        ans.append(li)
    print(ans)

addMarrix()



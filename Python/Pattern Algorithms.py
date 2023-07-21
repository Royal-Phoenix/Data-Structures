def Pyramid(n):
    k = 0
    for i in range(1,n+1):
        for j in range(1,(n-i)+1):
            print(" ",end="")
        while k!=(2*i - 1):
            print("*",end="")
            k += 1
        k = 0
        print()
def Level(n):
    k = 0
    for i in range(1,n+1):
        for j in range(1,(n-i)+1):
            print(" ",end="")
        while k!=(2*i - 1):
            print(i,end="")
            k += 1
        k = 0
        print()
def Number(n):
    k = 0
    for i in range(1,n+1):
        for j in range(1,(n-i)+1):
            print(" ",end="")
        while k!=(2*i - 1):
            print(k+1,end="")
            k += 1
        k = 0
        print()

print("\nMENU\n1.Pyramid Pattern\n2.Level Pattern\n3.Number Pattern\n\n")
choice = int(input("Enter the Choice : "))
if (1 <= choice <= 3):
    n = int(input("Enter the Number of Rows : "))
    if choice == 1:
        Pyramid(n)
    elif choice == 2:
        Level(n)
    else:
        Number(n)
else:
    print("Invalid Choice")

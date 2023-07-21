def Linear_Search(arr,key):
    for i in arr:
        if i == key:
            print(i,"is found at index",arr.index(i),"by Linear Search")

def Sentinel_Linear_Search(arr,key):
    end = arr[len(arr) - 1]
    arr[len(arr) - 1] = key
    i = 0
    while(arr[i] != key):
        i += 1
    arr[len(arr) - 1] = end
    print(key,"is found at index",i,"by Sentinel Linear Search")

def Binary_Search(arr,x,y,key):
    mid = (x + y) // 2
    if key < arr[mid]:
        Binary_Search(arr,x,mid-1,key)
    elif key > arr[mid]:  
        Binary_Search(arr,mid+1,y,key)
    else:
        print(key,"is found at index",mid,"by Binary Search")

def Ternary_Search(arr,x,y,key):
    if y >= x:
        mid1 = x + ((y - 1) // 3)
        mid2 = y - ((y - 1) // 3)
        if key < arr[mid1]:
            return Ternary_Search(arr,x,mid1-1,key)
        elif key == arr[mid1]:
            return mid1
        elif key == arr[mid2]:
            return mid2
        elif key > arr[mid2]:
            return Ternary_Search(arr,mid2+1,y,key)
        else:
            return Ternary_Search(arr,mid1+1,mid2-1,key)

print("\nMENU\n1.Linear Search\n2.Sentinel Linear Search")
print("3.Binary Search\n4.Ternary Search\n\n")
choice = int(input("Enter the Choice : "))
if (1 <= choice <= 4):
    n = int(input("Enter the Number of Elements : "))
    arr = [int(input("Enter the Element : ")) for i in range(n)]
    key = int(input("Enter the Search Value : "))
    if choice == 1:
        Linear_Search(arr,key)
    elif choice == 2:
        Sentinel_Linear_Search(arr,key)
    elif choice == 3:
        Binary_Search(arr,0,n,key)
    else:
        ind = Ternary_Search(arr,0,n,key)
        print(key,"is found at index",ind,"by Ternary Search")
else:
    print("Invalid Choice")

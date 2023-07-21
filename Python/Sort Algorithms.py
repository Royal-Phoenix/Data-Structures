def Bubble_Sort(arr): # Sinking Sort # (n-1) ** 2 ways
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print("Sorted Array by Bubble Sort :",arr)

def Selection_Sort(arr):
    for i in range(len(arr)-1):
        min_ind = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_ind]:
                arr[j],arr[min_ind] = arr[min_ind],arr[j]
    print("Sorted Array by Selection Sort :",arr)

def Insertion_Sort(arr): # n*(n-1)/4
    for i in range(1,len(arr)):
        temp = arr[i]
        pos = i-1
        while (temp < arr[pos]) and (pos >= 0):
            arr[pos + 1] = arr[pos]
            pos -= 1
        arr[pos+1] = temp
    print("Sorted Array by Insertion Sort:",arr)

def Merge_Sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        ls,rs = arr[:mid],arr[mid:]
        Merge_Sort(ls)
        Merge_Sort(rs)
        i,j,k = 0,0,0
        while (i < len(ls)) and (j < len(rs)):
            if ls[i] < rs[j]:
                arr[k] = ls[i]
                i,k = i+1,k+1
            else:
                arr[k] = rs[j]
                j,k = j+1,k+1
        while i < len(ls):
            arr[k] = ls[i]
            i,k = i+1,k+1
        while j < len(rs):
            arr[k] = rs[j]
            j,k = j+1,k+1

def Partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def Quick_Sort(arr, low, high):
    if low < high:
        pi = Partition(arr, low, high)
        Quick_Sort(arr, low, pi - 1)
        Quick_Sort(arr, pi + 1, high)

print("\nMENU\n1.Bubble Sort\n2.Selection Sort\n3.Insertion Sort")
print("4.Merge Sort\n5.Quick Sort\n\n")
choice = int(input("Enter the Choice : "))
if (1 <= choice <= 5):
    n = int(input("Enter Number of Elements : "))
    arr = [int(input("Enter a Number : ")) for i in range(n)]
    if choice == 1:
        Bubble_Sort(arr)
    elif choice == 2:
        Selection_Sort(arr)
    elif choice == 3:
        Insertion_Sort(arr)
    elif choice == 4:
        Merge_Sort(arr)
        print("Sorted Array by Merge Sort :",arr)
    else:
        Quick_Sort(arr, 0, len(arr) - 1)
        print("Sorted array by Quick Sort :",arr)
else:
    print("Invalid Choice")

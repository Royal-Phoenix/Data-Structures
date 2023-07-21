class Array:
    def __init__(self):
        self.arr = []
        
    def Append(self):
        data = int(input("Enter the Value to Append : "))
        self.arr.append(data)
    
    def Create(self):
        num = int(input("Enter the Number of Elements : "))
        for i in range(num):
            x = int(input("Enter Value : "))
            self.arr.append(x)
    
    def Insert(self):
        data = int(input("Enter the Value to Insert : "))
        ind = int(input("Enter the Index to Insert : "))
        self.arr.insert(ind,data)
    
    def Pop(self):
        self.arr.pop()
        print("Array Elements after Popping")
    
    def Remove(self):
        data = int(input("Enter the Value to Remove : "))
        self.arr.remove(data)
    
    def Delete(self):
        ind = int(input("Enter the Index to Delete : "))
        del self.arr[ind]
     
    def Update(self):
        data = int(input("Enter the Value to Update : "))
        ind = int(input("Enter the Index to Update : "))
        self.arr[ind] = data
        
    def Count(self):
        print("Array Length :",len(self.arr))
        
    def Search(self):
        data = int(input("Enter the Value to Search : "))
        print("Element",data,"found at Index",self.arr.index(data))
        
    def Sort(self):
        self.arr.sort()
        print("Array Elements after Sorting")
        
    def Reverse(self):
        self.arr.reverse()
        print("Array Elements after Reversing")
        
    def Display(self):
        print(self.arr)
        
obj = Array()
obj.Create()
obj.Display()
obj.Count()
obj.Search()
obj.Sort()
obj.Display()
obj.Reverse()
obj.Display()

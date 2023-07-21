class Hash_Map:
    def Hashing(self,key):
        return key%len(HashTable)

    def insert(self,HashTable,key,val):
        Hash_Key = self.Hashing(key)
        HashTable[Hash_Key].append(val)
        
    def display(self,HashTable):
        for i in range(len(HashTable)):
            print(i,end = " ")
            for j in HashTable[i]:
                print("-->",end = " ")
                print(j,end = " ")
            print()

HashTable = [[] for i in range(10)]
obj = Hash_Map()
n = int(input("Enter the Number of Elements : "))
for i in range(n):
    key = int(input("Enter Key Value : "))
    val = str(input("Enter Value : "))
    obj.insert(HashTable,key,val)
obj.display(HashTable)
print(HashTable)

class Heap:
    def __init__(self):
        self.arr = []
        self.arr.append(-1)
        self.size = 0
    
    def insert(self,value):
        self.size += 1
        index = self.size
        self.arr.append(value)

        while(index > 1):
            parent = int(index/2)
            if (self.arr[parent]<self.arr[index]):
                self.arr[parent],self.arr[index] = self.arr[index],self.arr[parent]
                index = parent
            else:
                return
h = Heap()

array = [50,70,40,10,20, 100]
for i in array:
    h.insert(i)
print(h.arr)
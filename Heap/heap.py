class Heap:
    def __init__(self):
        self.arr = []
        self.size = 0
    
    def insert(self,value): 
        index = self.size
        self.arr.append(value)
        self.size += 1

        while(index > 0):
            parent = int((index-1)/2)
            if (self.arr[parent]<self.arr[index]):
                self.arr[parent],self.arr[index] = self.arr[index],self.arr[parent]
                index = parent
            else:
                return

    

    def heapify(self,target, heapSize):
        largest = target
        left = 2 * target +1
        right= 2 * target +2

        if (left< heapSize and self.arr[left]>self.arr[largest]):
            largest = left
        if (right< heapSize and self.arr[right]>self.arr[largest]):
            largest = right

        if (largest != target):
            self.arr[target],self.arr[largest] = self.arr[largest],self.arr[target]
            self.heapify(largest, heapSize)


    def extract(self):
        if (self.size == 0):
            return

        self.arr[0],self.arr[self.size -1] = self.arr[self.size-1], self.arr[0]
        self.size -= 1

        self.heapify(0,self.size)

    def heapSort(self):
        n = self.size

        while (n>1):
            self.arr[0],self.arr[n-1] = self.arr[n-1],self.arr[0]
            n -= 1
            self.heapify(0, n)




    def printHeap(self):
        i = 0
        printArr = []
        while (i < self.size):
            printArr.append(self.arr[i])
            i +=1
        print(printArr)



h = Heap()

array = [50,70,40,10,20, 100]
for i in array:
    h.insert(i)

h.heapSort()

# for j in range(len(array)):
#     h.extract()

# print("after extraction")
# h.extract()
# print("size:", h.size)

# h.printHeap()

print(h.arr)
h.printHeap()


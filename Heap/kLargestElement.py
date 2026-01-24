import heapq

def kLargestElementBruteForce(arr,k):
    out = []
    while (k>0):
        largest = 0
        for i in range(len(arr)):
            if (arr[largest]<arr[i]):
                largest = i
        out.append(arr[largest])
        arr.remove(arr[largest])
        k-=1
    out.reverse()
    return out


def kLargestElementSort(arr,k):
    arr.sort()
    return arr[-k:]

def kLargestElement(arr,k):
    out = []
    for i in arr:
        heapq.heappush(out,i)
        if len(out)> k:
            heapq.heappop(out)
    return out


arr = [5,1,3,2,4,6]
print(kLargestElement(arr,2))



            
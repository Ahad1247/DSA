import time

st = time.process_time()
array = list(map(int, input().split()))

def insSort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j-1],arr[j]= arr[j],arr[j-1]
            j-=1
    return arr


print(insSort(array))
et = time.process_time()

print("Running time",et-st)

def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        j = i
        minIndex = i
        while(j<n):
            if (arr[j]<arr[minIndex]):
                minIndex = j
            j+=1
        arr[i],arr[minIndex]=arr[minIndex],arr[i]

ary = [4,3,1,7,2]
selectionSort(ary)
print(ary)
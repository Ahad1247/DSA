def selectionSort(arr):
    for i in range(len(arr)):
        j = i
        minIndex = i
        while(j<len(arr)):
            if (arr[j]<arr[minIndex]):
                minIndex = j
            j+=1
        arr[i],arr[minIndex]=arr[minIndex],arr[i]

ary = [4,3,1,7,2,1]
selectionSort(ary)
print(ary)
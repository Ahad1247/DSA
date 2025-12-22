def pivot(arr,low,high):
    initialPivot = arr[low]
    i = low
    j = high
    while(i<j):
        while(arr[i] <= initialPivot and i <= high-1):
            i += 1
        while(arr[j] > initialPivot and j>= low+1):
            j -= 1
        if (i<j):
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[low],arr[j] = arr[j],arr[low]
    
    return j


def quickSort(arr,low,high):
    if (low>=high):
        return
    
    pivotIndex = pivot(arr,low,high)

    quickSort(arr,low,pivotIndex-1)
    quickSort(arr,pivotIndex+1,high)


array = [4,7,2,3,9,8,1,5,6,1,1]
quickSort(array,0,len(array)-1)
print(array)
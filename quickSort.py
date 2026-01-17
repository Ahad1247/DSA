def pivot(arr,low,high):
    # initial pivot
    pivot = arr[low]
    i = low
    j = high

    # check until i and j cross each other
    while (i<j):
        # Skip smaller value than pivot to find the larger value
        while(arr[i] <= pivot and i <= high-1):
            i+=1

        # Skip larger value than pivot to find the smaller value
        while(arr[j] > pivot and j >= low+1):
            j-=1
        
        # if i and j doesn't cross each other, then swap arr[i] and arr[j]
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    
    # Swapping pivot and arr[j] because i and j has crossed each other
    arr[low],arr[j]=arr[j],arr[low]

    # return the actual pivot index
    return j


def quickSort(arr,low,high):
    if (low>=high):
        return
    
    pivotIndex = pivot(arr,low,high)

    #left portion
    quickSort(arr,low,pivotIndex-1)
    
    #right portion
    quickSort(arr,pivotIndex+1,high)

array = [4,7,2,3,9,8,1,5,6]
quickSort(array,0,len(array)-1)
print(array)

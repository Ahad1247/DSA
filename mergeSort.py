def merge(arr,low,mid,high):
    left = low
    right = mid+1
    temp = []

    while(left <= mid and right <= high):
        if arr[left]<= arr[right]:
            temp.append(arr[left])
            left+= 1
        else:
            temp.append(arr[right])
            right+= 1

    while(left <= mid):
        temp.append(arr[left])
        left+= 1

    while(right <= high):
        temp.append(arr[right])
        right+= 1

    i = low
    while (i <= high):
        arr[i] = temp[i-low]
        i+= 1

def mergeSort(arr,low,high):
    #base case
    if (low==high):
        return
    
    mid = int((low+high)/2)
    #left side
    mergeSort(arr,low,mid)
    #right side
    mergeSort(arr,mid+1,high)
    merge(arr, low, mid, high)

array = [1,3,5,2,4,8,1,4]
print("before:",array)
mergeSort(array,0,len(array)-1)
print("after:",array)
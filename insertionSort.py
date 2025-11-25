def insertionSort(arr):
    for i in range(len(arr)):
        j = i

        while(j>0 and arr[j-1]>arr[j]):
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j -= 1
            
        print("round-",i," : ",arr)
    

list = [2,7,1,12,5,5,5,1,8,3,9]
print("before sorting: ",list)
insertionSort(list)
print("after sorting: ",list)
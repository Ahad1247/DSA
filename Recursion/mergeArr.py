def merge(arr1,arr2):
    i= 0
    j= 0
    m = len(arr1)
    n = len(arr2)
    newArr = []
    while(i<m and j<n):
        if arr1[i]<arr2[j]:
            newArr.append(arr1[i])
            i+=1
        else:
            newArr.append(arr2[j])
            j+=1
    while(i<m):
        newArr.append(arr1[i])
        i+=1
    while(j<n):
        newArr.append(arr2[j])
        j+=1
    return newArr

arr1 = [1,2,5,6]
arr2 = [3,4,8,9,10,11,12,13]
print(merge(arr1,arr2))
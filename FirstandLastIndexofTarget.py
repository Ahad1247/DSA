def findFirst(arr,t):
    s = 0
    e = len(arr)-1
    ans = -1 
    while(s<=e):
        mid = int(s+(e-s)//2)

        if arr[mid] == t:
            ans = mid
            e = mid-1
        elif arr[mid]>t:
            e = mid-1
        else:
            s=mid+1
    return ans

def findLast(arr,t):
    s = 0
    e = len(arr)-1
    ans = -1 
    while(s<=e):
        mid = int(s+(e-s)//2)

        if arr[mid] == t:
            ans = mid
            s = mid+1
        elif arr[mid]>t:
            e = mid-1
        else:
            s=mid+1
    return ans

array = [1,2,3,3,3,3,4,5,6]
print([findFirst(array,10), findLast(array,10)])

def getPivotIndex(arr, n):
    s = 0
    e = n - 1
    mid = s + (e - s) // 2

    while s < e:
        if arr[mid] >= arr[0]:
            s = mid + 1
        else:
            e = mid

        mid = s + (e - s) // 2

    return s


def binarySearch(nums,s,e,target):
    if len(nums)==1 and nums[0]==target:
        return 0
    while(s<=e):
        mid = int(s+(e-s)//2)
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            e = mid-1
        else:
            s = mid+1
    return -1




nums = [4,5,6,7,0,1,2]
n= len(nums)
pivot = getPivotIndex(nums,n)
print(pivot)
target = 5


if (target>=nums[pivot] and target<= nums[n-1]):

    index = binarySearch(nums,pivot,n-1,target)
    print("side at",index)
else:
    index = binarySearch(nums,0,pivot-1,target)
    print("side at",index)


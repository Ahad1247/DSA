def findPeakElement( nums) -> int:
    n = len(nums)
    if n==1:
        return 0
    if nums[0]> nums[1]:
        return 0
    if nums[n-1]>nums[n-2]:
        return n-1
    
    s = 1
    e = n-2

    while (s<=e):
        mid = int(s+(e-s)//2)
        if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
            return mid
        elif nums[mid]>nums[mid-1]:
            s = mid+1
        else:
            e = mid-1
    return -1

arr = [1,2,1,3]
print(findPeakElement(arr))
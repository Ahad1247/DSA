list =[1,2,3,4,5]

def binarySearch(target,list):
    s=0
    e=len(list)-1
    mid = int((s+e)/2)
    while(s<=e):
        if (list[mid]==target):
            return True
        if (target>list[mid]):
            s = mid + 1
        if (target<list[mid]):
            e = mid - 1
        mid = int((s+e)/2)
    return False

print(binarySearch(10,list))
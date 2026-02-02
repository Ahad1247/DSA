array = [9,8,7,6,5,4,3,2,1,0]


def reverseList(arr):
    start = 0
    end = len(arr)-1
    while(end > start):
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1
    return (arr)
print(reverseList(array))

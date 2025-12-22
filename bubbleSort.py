def bubbleSort(arr):
    n = len(arr)
    i = n-1
    while(i>=0):
        j=0

        while(j<i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
            j+=1

        i-=1

ary = [4,3,1,7,2,1,1,67,49,12,81]
bubbleSort(ary)
print(ary)


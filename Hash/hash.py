n = int(input("enter hash size: "))
hash = [0]*(n+1)
arr = []

while(n>0):
    arr.append(int(input()))
    n-=1

for i in range(len(arr)):
    hash[arr[i]]+=1

q = int(input("Enter number of search values:"))

while (q>0):
    search = int(input("Enter search value: "))
    
    print(f"Total number of {search} is {hash[search]}")
    q-=1
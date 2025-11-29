import sys
sys.setrecursionlimit(1000000)
def countN(i, n):
    if (i > n):
        return
    
    print(i)

    countN(i+1,n)
    

    
n = int(input("enter a number: "))
countN(1,n)
    
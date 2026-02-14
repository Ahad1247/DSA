x = int(input("Enter a positive integer: "))

def oneToN(n, i):
    if (i>n):
        return
    print(i,end = " ")
    oneToN(n, i+1)





oneToN(x,1)
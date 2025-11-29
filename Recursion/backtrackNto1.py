def NtoOne(i,n):
    if (i>n):
        return
    NtoOne(i+1,n)
    print(i)
NtoOne(1,5)
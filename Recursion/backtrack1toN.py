def oneToN(i):
    if (i<1):
        return
    print("call for:",i)
    oneToN(i-1)
    print(i)
    print("ahad")
oneToN(6)

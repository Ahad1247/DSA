def reverse(x: int) -> int:
    if x == 0:
        return x
    
    ans:int = 0

    if (x<0):
        sign = -1
    else:
        sign= 1
        
    x = abs(x)

    while (x!=0):
        digit = x % 10
        ans = ans*10 + digit
        x = x//10

    return ans*sign


print(reverse(-523))



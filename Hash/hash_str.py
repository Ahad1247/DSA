string = input("enter a string: ")
hash = [0]*256

for c in string:
    hash[ord(c)]+=1

q = int(input("Enter number of search values:"))

while (q>0):
    search = input("Enter search value: ")
    
    print(f"Total number of {search} is {hash[ord(search[0])]}")
    q-=1
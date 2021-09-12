def range_func(n):
    for i in range(1,n+1,1):
        start_char=chr(ord("A")+n-i)
        for j in range(1,i+1,1):
            print(chr(ord(start_char)+j-1),end="")
        print()

def while_func(n):
    i=1
    while i<=n:
        start_char = chr(ord("A") + n - i)
        j=1
        while j<=i:
            print(chr(ord(start_char) + j - 1), end="")
            j=j+1
        print()
        i=i+1
n=int(input())
while_func(n)
range_func(n)
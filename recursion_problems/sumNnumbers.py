def sumnNumber(n,sum):
    if n < 1:
        print(sum)
        return
    sumnNumber(n-1,sum+n)

n = int(input("enter a number ; "))
print(sumnNumber(n,0))
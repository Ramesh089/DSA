def fibo(n):
    if n<=1:
        return n
    last = fibo(n-1)
    slast = fibo(n-2)
    return last + slast


num = int(input("Enter a Number : "))

print(fibo(num))
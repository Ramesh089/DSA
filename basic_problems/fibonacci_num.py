num = int(input("Enter a Number : "))

last = 1
slast = 1
fibo = []
for i in range(1,num+1):
    fibo.append(last)
    last,slast = slast,last+slast


print(last)
print(fibo)
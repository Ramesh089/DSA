def factorial(n):
        fact = 1
        for i in range(1,n+1):
            fact = fact * i

        return fact

num = int(input("enter a Number : "))
print(factorial(num))
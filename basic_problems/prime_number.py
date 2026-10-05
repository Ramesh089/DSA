def primeNumber(num):

    if num < 0:
        return "Invalid number"

    if num < 2:
        return "Not a prime number"

    for i in range(2, num):
        if num % i == 0:
            return "Not a prime number"

    return "Prime number"


num = int(input("Enter a number: "))

print(primeNumber(num))


def countPrimeNumber(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count = count + 1

        if count == 2:
            print("prime Number")
        else:
            print("NOt a prime Number")

    return count


print(countPrimeNumber(num))
def odddigitNumber(num):
    num = abs(num)
    oddcount = 0 

    if num == 0:
        return 0

    while num > 0 :
        last_digit = num % 10
        num = num // 10
        if last_digit % 2 == 1:
            oddcount = oddcount + 1

    return oddcount

num = int(input("enter a number : "))

print(odddigitNumber(num))

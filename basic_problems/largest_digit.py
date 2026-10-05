def largetst_digit_in_number(num):
    largestNumber = 0
    while num > 0:
        last_digit = num % 10
        num = num // 10
        if last_digit > largestNumber:
            largestNumber = last_digit

    return largestNumber

num = int(input("enter a Number : "))
print(largetst_digit_in_number(num))

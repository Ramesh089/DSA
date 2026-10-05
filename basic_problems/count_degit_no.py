num = int(input("Enter a number : "))

# count = 0
# while num > 0 :
#     last_digit = num % 10
#     count = count + 1
#     num = num // 10

# print(count)


num = abs(num)

def countDigit(num):
    num = abs(num)
    count = 0
    if num == 0 :
        return 1

    while num > 0:
        last_digit = num % 10
        count = count + 1
        num = num // 10

    return count
num = int(input("Enter a number : "))

count = 0
while num > 0 :
    last_digit = num % 10
    count = count + 1
    num = num // 10

print(count)
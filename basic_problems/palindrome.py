num = int(input("Enter a number : "))

revNum = 0
dupNum = num

while num > 0:
    last_degit = num % 10
    num = num // 10
    revNum = (revNum*10)+last_degit


if revNum == dupNum:
    print("yes, its palindrome number......")
else:
    print("No, it's not palindrome number....")
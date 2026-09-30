num = int(input("enter a number  : "))
revNum = 0
while num > 0:
    last_degit = num%10
    num = num //10
    revNum = (revNum*10)+last_degit

print(revNum)
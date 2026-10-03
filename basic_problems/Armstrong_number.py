num = int(input("Enter a Number :"))

sum1 = 0 
duplt_num = num 
# revNum = 0
while num > 0:
    last_degit = num % 10
    sum1 = sum1 + last_degit * last_degit * last_degit
    num = num //10
    # revNum = (revNum*10)+last_degit

if sum1 == duplt_num:
    print("Given number is Armstrong ")
else:
    print("The Given Number  is not Armstrong ")

 
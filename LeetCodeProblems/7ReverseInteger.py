num = int(input("enter a number : "))

if num < 0:
    sign = -1
else:
    sign  = 0

num = abs(num)
revInt = 0
while num > 0:
    lastdigit = num % 10
    num = num // 10
    revInt = (revInt*10)+lastdigit

revInt = revInt * sign

if revInt > 2**31 -1 or revInt < -2 ** 31:
    revInt = 0

print(revInt)
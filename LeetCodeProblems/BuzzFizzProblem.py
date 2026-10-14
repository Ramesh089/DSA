n = 15
strList = []

for i in range(1,n+1):
    if i % 3 ==0 and i % 5 ==0:
        strList.append("BuzzFizz")
    elif i % 3 == 0:
        strList.append("Fizz")
    elif i % 5 == 0:
        strList.append("Buzz")
    else:
        strList.append(str(i))

print(strList)
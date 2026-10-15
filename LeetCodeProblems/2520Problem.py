num = 1248
count = 0 
dupNum = num

while num > 0 :
    lastdigit = num % 10
    num = num // 10

    if dupNum % lastdigit == 0:
        count = count + 1


print(count)
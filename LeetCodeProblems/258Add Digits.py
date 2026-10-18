num = 38

add = 0
while num > 0:
    lastdigt = num % 10
    num = num //10
    add = add + lastdigt

    while add > 9:
        total = 0
        while add > 0:
            lastdigt = add % 10
            add = add // 10
            total += lastdigt

        add = total

print(add)
        
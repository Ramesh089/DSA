nums = [12,345,2,6,7896]
count = 0
for i in nums:
    digits = len(str(i))

    if digits % 2 == 0 :
        count+=1

print(count)
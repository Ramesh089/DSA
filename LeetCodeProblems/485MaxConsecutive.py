nums = [1,0,1,1,0,1,1,1]
count = 0 
maxcount = 0

for i in nums:
    if i == 1:
        count = count + 1
    else:
        count = 0 

    if count > maxcount :
        maxcount = count

    # maxcount = max(maxcount,count)


print(maxcount)
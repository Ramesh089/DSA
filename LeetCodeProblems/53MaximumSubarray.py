nums = [-2,1,-3,4,-1,2,1,-5,4]

curSum = 0
maxSum = nums[0]

for st in range(len(nums)):
    curSum = 0
    for end in range(st,len(nums)):
        curSum +=nums[end]

        maxSum = max(curSum,maxSum)

    # print(curSum)

print(maxSum)    
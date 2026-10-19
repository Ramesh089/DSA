# satisfied approach

nums = [1,2,3]

if len(nums) != len(set(nums)):
    # return True 
    print(True)
else:
    print(False)



# other approach
count = 0
for i in range(len(nums)):
    for j in range(i + 1,len(nums)):
        if nums[i] == nums[j]:
            count+=1

if count >=1:
    print(True)
else:
    print(False)

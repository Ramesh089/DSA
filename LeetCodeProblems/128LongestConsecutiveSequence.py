def longestseqlght(nums):
    num_set  = set(nums)
    longest = 0
    for i in range(len(nums)):
        count = 1
        current = i
        if i-1 not in num_set:
            while current+1 in num_set:
                count+=1
                current+=1

            longest = max(longest,count)


    return longest
nums = [100,4,200,1,3,2]
print(longestseqlght(nums))
def longestseqlght(nums):
    set_nums = set(nums)

    longest=0
    for i in set_nums:
        count = 1
        current = i
        if i-1 not in set_nums:
            while current+1 in set_nums:
                count +=1
                current+=1

        longest = max(count,longest)

    return longest
nums = [100,4,200,1,3,2]
print(longestseqlght(nums))
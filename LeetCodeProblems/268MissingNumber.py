def missingNumber(nums):
    xor1 =0
    xor2 = 0
    for i in range(len(nums)):
        xor1 = xor1^i
        xor2 = xor2^nums[i]

    xor1 = xor1^len(nums)

    return xor1^xor2

nums = [3,0,1]

print(missingNumber(nums))


# better aproach
n = len(nums)
sum = n * (n+1)/2
s2 = 0
for i in range(len(nums)):
    s2 += nums[i]

print(sum-s2)
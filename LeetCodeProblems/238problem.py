# 238. Product of Array Except Self
def roductExceptSelf(nums):
    n = len(nums)
    ans = [1]*n

    for i in range(1,n):
        ans[i] = ans[i-1]*nums[i-1]

    suffix = 1
    for i in range(n-2,-1,-1):
        suffix*=nums[i+1]
        ans[i]*=suffix

    return ans



nums = [1,2,3,4]
print(roductExceptSelf(nums))
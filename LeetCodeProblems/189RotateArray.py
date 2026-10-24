# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]


nums = [1,2,3,4,5,6,7]
k = 3

n = len(nums)
k%=n

nums[:] = nums[::-1]
nums[:k] = nums[:k][::-1]
nums[k:] = nums[k:][::-1]


print(nums)
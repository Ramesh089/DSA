# class Solution:
#     def leaders(self, nums):
#         ans = []
#         maxi = float('-inf')
#         n = len(nums)

#         for i in range(n - 1, -1, -1):
#             if nums[i] >= maxi:
#                 ans.append(nums[i])

#             maxi = max(maxi, nums[i])

#         ans.reverse()
#         return ans


nums = [1, 2, 5, 3, 1, 2]

ans = []
maxi = float('-inf')
n = len(nums)

for i in range(n - 1, -1, -1):
    if nums[i] >= maxi:
        ans.append(nums[i])

    maxi = max(maxi, nums[i])

ans.reverse()
print(ans)
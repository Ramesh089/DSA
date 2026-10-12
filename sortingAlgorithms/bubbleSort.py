# class Solution:
#     def bubbleSort(self, nums):
#         for i in range(len(nums)):
#             for j in range(n-i-1):
#                 if nums[j]>nums[j+1]:
#                     nums[j],nums[j+1] = nums[j+1],nums[j]

#         return nums


arr = [34,29,56,78,45,23]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)
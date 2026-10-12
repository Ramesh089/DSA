# class Solution:
#     def selectionSort(self, nums):
#         n = len(nums)

#         for i in range(n):
#             min = i
#             for j in range(i+1,n):
#                 if nums[j] < nums[min]:
#                     min = j

#                 nums[i],nums[min] = nums[min],nums[i]

#         return nums


arr = [47,45,34,22,82]
n=len(arr)

for i  in range(n):
    min = i
    for j in range(i+1,n):
        if arr[j]<arr[min]:
            min = j

    arr[i],arr[min]=arr[min],arr[i]

print(arr)


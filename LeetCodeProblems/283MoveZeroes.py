# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         temp = []

#         for i in range(len(nums)):
#             if nums[i] !=0:
#                 temp.append(nums[i])

#         nz = len(temp)

#         for i in range(nz):
#             nums[i] = temp[i]

#         for i in range(nz,len(nums)):
#             nums[i] = 0

#         return nums




def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = []

        for i in range(len(nums)):
            if nums[i] !=0:
                temp.append(nums[i])

        nz = len(temp)

        for i in range(nz):
            nums[i] = temp[i]

        for i in range(nz,len(nums)):
            nums[i] = 0

        return nums


nums = [0,1,0,3,12]
moveZeroes(nums)
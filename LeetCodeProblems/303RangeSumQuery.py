
# class NumArray:

#     def __init__(self, nums):
#         self.prefix_sum = [0] * (len(nums) + 1)

#         for i in range(len(nums)):
#             self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

#     def sumRange(self, left, right):
#         return self.prefix_sum[right + 1] - self.prefix_sum[left]
class NumArray(object):

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        total = 0

        for i in range(left, right + 1):
            total += self.nums[i]

        return total
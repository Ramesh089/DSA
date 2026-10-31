# class Solution(object):
def subarraySum(nums, k):
        presum = 0
        cnt = 0
        map = {0: 1}

        for i in range(len(nums)):
            presum += nums[i]

            remove = presum - k

            cnt += map.get(remove, 0)

            map[presum] = map.get(presum, 0) + 1

        return cnt


nums = [1,1,1]
k = 2

print(subarraySum(nums,k))
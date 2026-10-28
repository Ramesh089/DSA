def rearrangeArray(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n =len(nums)
        ans = [0]*n
        posidx = 0
        negidx =1
        for i in range(n):
            if nums[i] < 0:
                ans[negidx] = nums[i]
                negidx +=2
            else:
                ans[posidx] = nums[i]
                posidx +=2

        return ans


nums = [3,1,-2,-5,2,-4]
print(rearrangeArray(nums))
# 88. Merge Sorted Array

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        left = m - 1
        right = 0

        while left >= 0 and right < n:
            if nums1[left] > nums2[right]:
                nums1[left], nums2[right] = nums2[right], nums1[left]
                left -= 1
                right += 1
            else:
                break

        nums1[:m] = sorted(nums1[:m])
        nums2[:n] = sorted(nums2[:n])

        for i in range(n):
            nums1[m + i] = nums2[i]
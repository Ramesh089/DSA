# You are given an array nums with n objects colored red, white,
#  or blue, sort them in-place so that objects of the same color are adjacent,
#  with the colors in the order red, white, and blue.

def sortColor(nums):
    end = len(nums)-1
    start = 0
    mid = 0
    while mid<=end:
        if nums[mid] == 0:
            nums[start],nums[mid] = nums[mid],nums[start]
            mid+=1
            start +=1

        elif nums[mid] == 1:
            mid+=1
        else:
            nums[mid],nums[end] = nums[end],nums[mid]

            end-=1

    return nums


nums = [2,0,2,1,1,0]
print(sortColor(nums))


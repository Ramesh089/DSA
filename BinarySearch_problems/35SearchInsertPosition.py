def seachinsertPosition(nums,target):
    low = 0
    high = len(nums)-1

    while low<high:

        mid = (low+high)//2

        if nums[mid] == target:
            high = mid
        else:
            low = mid+1

    return low


nums = [1,3,5,6]
target = 5
print(seachinsertPosition(nums,target))

# ....................................................Brute force approach............................................
def findDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] ==  nums[j]:
                return nums[i]

# ....................................................better approach..................................................

def findDuplicate(nums):
    dp = set()
    for i in range(len(nums)):
        if nums[i] in dp:
            return nums[i]

        dp.add(nums[i]) 

    return dp   
# ...................................optimal approach using the linked list concept....................................
def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


nums = [1,3,4,2,2]
print(findDuplicate(nums))
# You are given an integer array nums.

# Return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

# Example 1:

# Input: nums = [3,2,1]
# Output: 1

nums = [3,2,1]
first = None
second = None
third = None
for i in nums:
    if i == first or i == second or i == third:
        continue

    if first is None or i > first:
        third = second 
        second = first 
        first = i

    elif second is None or i > second:
        third = second 
        second = i
    elif third is None or i > third:
        third = i

    # if third is None :
    #     print(third)

print(third)

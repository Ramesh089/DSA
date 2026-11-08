
# .................................Brute Force approach....................................

def threeSum(nums):
    ans = []
    st = set()

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):

                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    st.add(tuple(temp))

    for item in st:
        ans.append(list(item))

    return ans


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))




# ................................better solution .................................

def threeSum(nums):
    st = set()

    for i in range(len(nums)):
        hashset = set()

        for j in range(i + 1, len(nums)):

            third = -(nums[i] + nums[j])

            if third in hashset:
                temp = [nums[i], nums[j], third]
                temp.sort()

                st.add(tuple(temp))

            hashset.add(nums[j])

    ans = [list(item) for item in st]

    return ans


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))





# .................................optimal solutin ...............................
def threeSum(nums):
    ans = []
    nums.sort()

    for i in range(len(nums)):

        if i > 0 and nums[i] == nums[i-1]:
            continue

        j = i + 1
        k = len(nums) - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total < 0:
                j += 1

            elif total > 0:
                k -= 1

            else:
                temp = [nums[i], nums[j], nums[k]]
                ans.append(temp)

                j += 1
                k -= 1

                while j < k and nums[j] == nums[j-1]:
                    j += 1

                while j < k and nums[k] == nums[k+1]:
                    k -= 1

    return ans

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
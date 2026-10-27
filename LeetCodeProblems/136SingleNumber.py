def singleNumber(nums):
    xor = 0
    for i in range(len(nums)):
        xor = xor ^ nums[i]

    return xor 


nums = [2,2,1]

print(singleNumber(nums))



#  Brute force approach 
def singleNumber1(nums):
      for i in range(len(nums)):
            count =0
            num = nums[i]
            for j in range(len(nums)):
                if nums[j] == num:
                    count+=1

            if count == 1:
                return num


print(singleNumber1(nums))



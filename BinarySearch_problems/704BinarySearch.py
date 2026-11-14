# .................................Binary search algorithm.....................................
def search(nums, target):
        s = 0
        e = len(nums) - 1

        while s <= e:
            mid = s + (e - s) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                e = mid - 1
            else:
                s = mid + 1

        return -1


nums = [-1,0,3,5,9,12]
target = 9
print(search(nums,target))



# .......................................Binary search with recursion algorithm...........................................

def recursionsearch(nums,low,high,target):
     if low > high:
          return -1
     mid = (low+high)//2

     if nums[mid] == target:
          return mid
     elif nums[mid] > target:
          return recursionsearch(nums,low,mid-1,target)
     else:
          return recursionsearch(nums,mid+1,high,target)



res = recursionsearch(nums,0,len(nums)-1,target)
print(res)

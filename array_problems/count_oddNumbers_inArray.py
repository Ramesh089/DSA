n = int(input("enter a size of array : "))
arr = []
for i in range(1,n+1):
    arrElement = int(input("enter the elements of Array : "))
    arr.append(arrElement)

count = 0
for i in arr:
    if i % 2 !=0:
        count = count+1

print(count)



# class Solution:
#     def countOdd(self, arr, n):
#         # Your code goes here
#         count = 0
#         for i in arr:
#             if i % 2 !=0:
#                 count = count+1

#         return count
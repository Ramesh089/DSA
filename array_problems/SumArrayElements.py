num = int(input("enter a number arr ..."))
arr = []
for i in range(1,num+1):
    arrElements = int(input("enter the arrElements : "))
    arr.append(arrElements)
sum = 0
for i in arr:
    sum = sum + i


print(sum)


# class Solution:
#     def sum(self,arr, n):
#         sum = 0
#         for i in arr:
#             sum = sum + i

#         return sum
    
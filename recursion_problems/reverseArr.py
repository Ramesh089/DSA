def reverArr(l, r):
    if l >= r:
        return

    a[l], a[r] = a[r], a[l]

    reverArr(l + 1, r - 1)


a = [1, 2, 3, 4, 5]
reverArr(0, len(a) - 1)

print(a)



# class Solution:
#     def reverse(self, arr: list, n: int) -> None:

#         def helper(l,r):
#             if l>=r:
#                 return
            
#             arr[l],arr[r] = arr[r],arr[l]

#             helper(l+1,r-1)

#         helper(0,n-1)
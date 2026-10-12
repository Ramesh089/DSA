# Largest Odd Number in a String

# class Solution:  
#     def largeOddNum(self, s: str) -> str:
#         #your code goes here
        
#         for i in range(len(s)-1,-1,-1):
#             if int(s[i]) %2 !=0:
#                 return s[:i+1].lstrip("0")

#         return ""

str = "008044227"

for i in range(len(str)-1,-1,-1):
    if int(str[i]) % 2!=0:
        print(str[:i+1].lstrip("0"))
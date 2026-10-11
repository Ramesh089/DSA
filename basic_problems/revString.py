# class Solution:
#     def reverseString(self,s):
#         #your code goes here
#         revstring = s[::-1]
#         dupstring = []
#         for i in revstring:
#             dupstring.append(i)

#         return dupstring

def reverseString(s):
        #your code goes here
        revstring = s[::-1]
        dupstring = []
        for i in revstring:
            dupstring.append(i)

        return dupstring



string = input("Enter a string  value :")
print(reverseString(string))
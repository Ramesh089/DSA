# class Solution:    
#     def palindromeCheck(self, s):
#         #your code goes here

#         revString = s[::-1]
#         dupString = s

#         if revString == dupString:
#             return True
#         else:
#             return False




def palindromeCheck(s):
        #your code goes here

        revString = s[::-1]
        dupString = s

        if revString == dupString:
            return True
        else:
            return False
        

string = input("Enter a string  value :")
print(palindromeCheck(string))
def reverseArray(s):
    left = 0
    right = len(s) - 1

    while left<right:
        s[left],s[right] = s[left],s[right]

        left +=1
        right -=1

    return left


str = input("Enter a  String : ")
print(reverseArray(str))


from collections import Counter
s = "anagram"
t = "nagaram"



if len(s) != len(t):
    print(False)

s_dict = Counter(s)
t_dict = Counter(t)

print(s_dict==t_dict)
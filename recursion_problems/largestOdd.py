# Largest Odd Number in a String

str = "008044227"

for i in range(len(str)-1,-1,-1):
    if int(str[i]) % 2!=0:
        print(str[:i+1].lstrip("0"))
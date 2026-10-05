
def isPerfect(n):
        count = 0
        for i in range(1,n):
            if n % i == 0:
                count = count + i

        if count == n:
            return True
        else:
            return False

num = int(input("enter a Number : "))
print(isPerfect(num))
def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        while i * i <= x:
            i +=1

        return i - 1


x = 4
print(mySqrt(x))
class Solution:
    def primeUptoN(self, num):
        count = 0

        for n in range(2, num + 1):
            is_prime = True

            for i in range(2, n):
                if n % i == 0:
                    is_prime = False
                    break

            if is_prime:
                count += 1

        return count
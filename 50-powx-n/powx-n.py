class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        ans = 1

        while n:
            if n % 2:
                ans *= x
            x *= x
            n //= 2

        return ans
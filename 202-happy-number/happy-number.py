class Solution:
    def isHappy(self, n):

        def squareSum(n):

            total = 0

            while n:

                digit = n % 10
                total += digit * digit
                n //= 10

            return total

        slow = n
        fast = n

        while True:

            slow = squareSum(slow)

            fast = squareSum(squareSum(fast))

            if slow == fast:
                break

        return slow == 1
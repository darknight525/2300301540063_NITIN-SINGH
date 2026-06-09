
class Solution:
    def missingNumber(self, nums):

        n = len(nums)

        expected = n * (n + 1) // 2

        actual = sum(nums)

        return expected - actual

        
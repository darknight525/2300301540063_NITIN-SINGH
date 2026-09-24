class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            num = nums[i]
            total = 0

            while num > 0:
                total += num % 10
                num //= 10

            if total == i:
                return i

        return -1
        
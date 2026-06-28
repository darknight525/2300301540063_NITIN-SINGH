class Solution:
    def findErrorNums(self, nums):

        seen = set()
        dup = 0

        for num in nums:
            if num in seen:
                dup = num
            seen.add(num)

        for i in range(1, len(nums) + 1):
            if i not in seen:
                return [dup, i]
        
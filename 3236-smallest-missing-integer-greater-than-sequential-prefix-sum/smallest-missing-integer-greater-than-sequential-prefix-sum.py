class Solution(object):
    def missingInteger(self, nums):
        total = nums[0]

        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        while total in nums:
            total += 1

        return total
        
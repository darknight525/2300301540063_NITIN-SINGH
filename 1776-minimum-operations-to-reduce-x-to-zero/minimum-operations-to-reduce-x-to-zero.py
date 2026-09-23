class Solution(object):
    def minOperations(self, nums, x):
        total = sum(nums)
        target = total - x

        if target < 0:
            return -1

        left = 0
        current = 0
        longest = -1

        for right in range(len(nums)):
            current += nums[right]

            while current > target:
                current -= nums[left]
                left += 1

            if current == target:
                longest = max(longest, right - left + 1)

        if longest == -1:
            return -1

        return len(nums) - longest
        
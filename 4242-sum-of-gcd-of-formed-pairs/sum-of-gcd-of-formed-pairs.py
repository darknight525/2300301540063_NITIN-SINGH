class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdSum(self, nums):
        n = len(nums)
        prefixGcd = [0] * n

        mx = 0
        for i in range(n):
            if nums[i] > mx:
                mx = nums[i]
            prefixGcd[i] = self.gcd(nums[i], mx)

        prefixGcd.sort()

        ans = 0
        for i in range(n // 2):
            ans += self.gcd(prefixGcd[i], prefixGcd[n - 1 - i])

        return ans
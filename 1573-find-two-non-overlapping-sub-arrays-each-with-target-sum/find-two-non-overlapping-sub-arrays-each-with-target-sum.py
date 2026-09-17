class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = 1000000

        dp = [INF] * n
        left = 0
        total = 0
        best = INF
        ans = INF

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                if left > 0:
                    ans = min(ans, length + dp[left - 1])

                best = min(best, length)

            dp[right] = best

        if ans == INF:
            return -1

        return ans
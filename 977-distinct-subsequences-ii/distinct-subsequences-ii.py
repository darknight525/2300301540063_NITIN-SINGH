class Solution(object):
    def distinctSubseqII(self, s):
        MOD = 1000000007

        dp = [0] * 26
        total = 0

        for ch in s:
            i = ord(ch) - ord('a')

            add = total - dp[i] + 1

            total = (total + add) % MOD
            dp[i] = (dp[i] + add) % MOD

        return total
        
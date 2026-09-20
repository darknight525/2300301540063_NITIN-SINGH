class Solution(object):
    def reverseDegree(self, s):
        ans = 0

        for i in range(len(s)):
            value = ord(s[i]) - ord('a') + 1
            reverse = 26 - value + 1

            ans += reverse * (i + 1)

        return ans
        
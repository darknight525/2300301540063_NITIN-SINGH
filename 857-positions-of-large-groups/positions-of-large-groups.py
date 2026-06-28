class Solution:
    def largeGroupPositions(self, s):

        ans = []
        i = 0

        while i < len(s):

            j = i

            while j < len(s) and s[j] == s[i]:
                j += 1

            if j - i >= 3:
                ans.append([i, j - 1])

            i = j

        return ans
        
class Solution:
    def longestPalindrome(self, s):

        result = ""

        for i in range(len(s)):

            # odd length
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:

                if (r - l + 1) > len(result):
                    result = s[l:r + 1]

                l -= 1
                r += 1

            # even length
            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:

                if (r - l + 1) > len(result):
                    result = s[l:r + 1]

                l -= 1
                r += 1

        return result
       
        
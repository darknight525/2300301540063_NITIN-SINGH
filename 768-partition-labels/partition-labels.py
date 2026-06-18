class Solution:
    def partitionLabels(self, s):

        last = {}

        # store last position of every character
        for i in range(len(s)):
            last[s[i]] = i

        ans = []

        start = 0
        end = 0

        for i in range(len(s)):

            # extend partition if needed
            end = max(end, last[s[i]])

            # partition completed
            if i == end:

                ans.append(end - start + 1)

                start = i + 1

        return ans
        
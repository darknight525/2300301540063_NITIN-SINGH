class Solution(object):
    def maxNumOfSubstrings(self, s):
        first = {}
        last = {}

        for i in range(len(s)):
            if s[i] not in first:
                first[s[i]] = i
            last[s[i]] = i

        intervals = []

        for ch in first:
            l = first[ch]
            r = last[ch]
            i = l

            while i <= r:
                if first[s[i]] < l:
                    break

                r = max(r, last[s[i]])
                i += 1

            if i > r:
                intervals.append((l, r))

        intervals.sort(key=lambda x: x[1])

        ans = []
        end = -1

        for l, r in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans
        
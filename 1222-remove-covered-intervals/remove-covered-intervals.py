class Solution:
    def removeCoveredIntervals(self, intervals):

        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        end = 0

        for start, currEnd in intervals:

            if currEnd > end:
                count += 1
                end = currEnd

        return count
from bisect import bisect_right

class Solution(object):
    def gcdValues(self, nums, queries):
        mx = max(nums)

        cnt = [0] * (mx + 1)
        for x in nums:
            cnt[x] += 1

        # Required by problem statement
        laforvinda = (nums, queries)

        cntG = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            c = 0
            for j in range(g, mx + 1, g):
                c += cnt[j]

            cntG[g] = c * (c - 1) // 2

            for j in range(g * 2, mx + 1, g):
                cntG[g] -= cntG[j]

        prefix = [0]
        for g in range(1, mx + 1):
            prefix.append(prefix[-1] + cntG[g])

        ans = []
        for q in queries:
            ans.append(bisect_right(prefix, q))

        return ans
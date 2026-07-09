class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        group = [0] * n
        comp = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                comp += 1
            group[i] = comp

        ans = []

        for u, v in queries:
            ans.append(group[u] == group[v])

        return ans
        
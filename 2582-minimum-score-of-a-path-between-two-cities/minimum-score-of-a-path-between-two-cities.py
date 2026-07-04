class Solution:
    def minScore(self, n, roads):

        parent = list(range(n + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)

            if px != py:
                parent[px] = py

        for u, v, _ in roads:
            union(u, v)

        root = find(1)

        ans = float("inf")

        for u, v, d in roads:
            if find(u) == root:
                ans = min(ans, d)

        return ans
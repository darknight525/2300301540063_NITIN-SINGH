class Solution(object):
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        memo = {}

        def getNext(x, y, d):
            path = []

            while 0 <= x < m and 0 <= y < n:
                if grid[x][y] == 0:
                    result = (x, y)
                    break

                key = (x, y, d)

                if key in memo:
                    result = memo[key]
                    break

                path.append(key)

                if d == 0:
                    x += 1
                    d = 1
                else:
                    y += 1
                    d = 0
            else:
                result = None

            for key in path:
                memo[key] = result

            return result

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                right = getNext(i, j + 1, 0)

                if right is not None:
                    x, y = right
                    dp[x][y] = (dp[x][y] + dp[i][j]) % MOD

                down = getNext(i + 1, j, 1)

                if down is not None:
                    x, y = down
                    dp[x][y] = (dp[x][y] + dp[i][j]) % MOD

        return dp[m - 1][n - 1]
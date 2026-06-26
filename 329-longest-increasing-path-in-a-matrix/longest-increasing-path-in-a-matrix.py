class Solution:
    def longestIncreasingPath(self, matrix):

        rows = len(matrix)
        cols = len(matrix[0])

        dp = {}

        def dfs(r, c):

            if (r, c) in dp:
                return dp[(r, c)]

            ans = 1

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:

                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    matrix[nr][nc] > matrix[r][c]
                ):

                    ans = max(ans, 1 + dfs(nr, nc))

            dp[(r, c)] = ans
            return ans

        res = 0

        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))

        return res
        
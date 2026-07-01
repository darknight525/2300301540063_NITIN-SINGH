from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid):

        n = len(grid)

        dist = [[-1] * n for _ in range(n)]
        q = deque()

        # Multi-source BFS from all thieves
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < n and
                    0 <= nc < n and
                    dist[nr][nc] == -1
                ):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        def can(x):

            if dist[0][0] < x:
                return False

            q = deque([(0, 0)])
            seen = {(0, 0)}

            while q:

                r, c = q.popleft()

                if (r, c) == (n - 1, n - 1):
                    return True

                for dr, dc in dirs:

                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < n and
                        0 <= nc < n and
                        (nr, nc) not in seen and
                        dist[nr][nc] >= x
                    ):

                        seen.add((nr, nc))
                        q.append((nr, nc))

            return False

        low = 0
        high = max(max(row) for row in dist)
        ans = 0

        while low <= high:

            mid = (low + high) // 2

            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
        
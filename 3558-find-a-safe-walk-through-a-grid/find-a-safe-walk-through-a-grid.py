from collections import deque

class Solution:
    def findSafeWalk(self, grid, health):

        m, n = len(grid), len(grid[0])

        health -= grid[0][0]

        if health <= 0:
            return False

        best = [[-1] * n for _ in range(m)]
        best[0][0] = health

        q = deque([(0, 0, health)])

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:

            r, c, hp = q.popleft()

            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in dirs:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:

                    newHp = hp - grid[nr][nc]

                    if newHp > 0 and newHp > best[nr][nc]:

                        best[nr][nc] = newHp
                        q.append((nr, nc, newHp))

        return False
        
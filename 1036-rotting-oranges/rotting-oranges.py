from collections import deque

class Solution:
    def orangesRotting(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 2:
                    q.append((r, c))

                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0

        while q and fresh:

            for _ in range(len(q)):

                r, c = q.popleft()

                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:

                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1
                    ):

                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            minutes += 1

        return minutes if fresh == 0 else -1
        
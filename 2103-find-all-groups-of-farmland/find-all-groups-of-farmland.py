class Solution:
    def findFarmland(self, land):

        rows = len(land)
        cols = len(land[0])

        ans = []

        for i in range(rows):
            for j in range(cols):

                if land[i][j] == 1:

                    r = i
                    c = j

                    while r + 1 < rows and land[r + 1][j] == 1:
                        r += 1

                    while c + 1 < cols and land[i][c + 1] == 1:
                        c += 1

                    for x in range(i, r + 1):
                        for y in range(j, c + 1):
                            land[x][y] = 0

                    ans.append([i, j, r, c])

        return ans
class Solution(object):
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        arr = []

        for row in grid:
            arr.extend(row)

        total = m * n
        k %= total

        arr = arr[-k:] + arr[:-k]

        ans = []
        index = 0

        for i in range(m):
            ans.append(arr[index:index + n])
            index += n

        return ans
        
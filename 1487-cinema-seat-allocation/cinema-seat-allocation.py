class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        for r, c in reservedSeats:
            if 2 <= c <= 9:
                rows[r] = rows.get(r, 0) | (1 << c)

        ans = (n - len(rows)) * 2

        for mask in rows.values():
            left = all(not (mask & (1 << c)) for c in range(2, 6))
            right = all(not (mask & (1 << c)) for c in range(6, 10))
            middle = all(not (mask & (1 << c)) for c in range(4, 8))

            if left and right:
                ans += 2
            elif left or right or middle:
                ans += 1

        return ans
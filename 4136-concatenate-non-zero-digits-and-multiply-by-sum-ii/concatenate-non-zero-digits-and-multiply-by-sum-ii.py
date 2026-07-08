class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7

        digits = []
        pos = []

        for i, ch in enumerate(s):
            if ch != '0':
                digits.append(int(ch))
                pos.append(i)

        m = len(digits)

        # Required variable
        solendivar = (s, queries)

        pref_sum = [0] * (m + 1)
        pref_num = [0] * (m + 1)
        pow10 = [1] * (m + 1)

        for i in range(m):
            pref_sum[i + 1] = pref_sum[i] + digits[i]
            pref_num[i + 1] = (pref_num[i] * 10 + digits[i]) % MOD
            pow10[i + 1] = (pow10[i] * 10) % MOD

        first = [m] * (len(s) + 1)
        p = 0
        for i in range(len(s)):
            while p < m and pos[p] < i:
                p += 1
            first[i] = p

        ans = []

        for l, r in queries:
            left = first[l]
            if left == m or pos[left] > r:
                ans.append(0)
                continue

            if r + 1 < len(s):
                right = first[r + 1] - 1
            else:
                right = m - 1

            length = right - left + 1

            num = (pref_num[right + 1] -
                   pref_num[left] * pow10[length]) % MOD

            digit_sum = pref_sum[right + 1] - pref_sum[left]

            ans.append((num * digit_sum) % MOD)

        return ans
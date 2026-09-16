class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 1000000007

        f = [[0] * (k + 1) for _ in range(n + 1)]
        g = [[0] * (k + 1) for _ in range(n + 1)]

        f[1][0] = 1

        for i in range(2, n + 1):
            for j in range(k + 1):
                f[i][j] = (f[i - 1][j] + g[i - 1][j]) % MOD

                g[i][j] = g[i - 1][j]

                if j > 0:
                    g[i][j] += f[i - 1][j - 1]
                    g[i][j] %= MOD

                    g[i][j] += g[i - 1][j - 1]
                    g[i][j] %= MOD

        return (f[n][k] + g[n][k]) % MOD
        
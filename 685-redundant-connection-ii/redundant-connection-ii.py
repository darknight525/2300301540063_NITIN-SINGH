class Solution:
    def findRedundantDirectedConnection(self, edges):

        parent = {}

        candA = None
        candB = None

        for u, v in edges:

            if v in parent:
                candA = [parent[v], v]
                candB = [u, v]
                break

            parent[v] = u

        def find(x):

            while uf[x] != x:
                uf[x] = uf[uf[x]]
                x = uf[x]

            return x

        def union(a, b):

            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False

            uf[pb] = pa
            return True

        uf = {}

        for i in range(1, len(edges) + 1):
            uf[i] = i

        for u, v in edges:

            if [u, v] == candB:
                continue

            if not union(u, v):

                if candA:
                    return candA

                return [u, v]

        return candB
        
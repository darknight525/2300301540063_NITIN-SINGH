from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n, edges):

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):

            visited.add(node)

            nodes = 1
            edgeCount = len(graph[node])

            for nei in graph[node]:

                if nei not in visited:

                    nNodes, nEdges = dfs(nei)

                    nodes += nNodes
                    edgeCount += nEdges

            return nodes, edgeCount

        ans = 0

        for i in range(n):

            if i not in visited:

                nodes, edgeCount = dfs(i)

                edgeCount //= 2

                if edgeCount == nodes * (nodes - 1) // 2:
                    ans += 1

        return ans
        
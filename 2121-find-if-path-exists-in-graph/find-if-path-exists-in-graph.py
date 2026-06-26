from collections import defaultdict

class Solution:
    def validPath(self, n, edges, source, destination):

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):

            if node == destination:
                return True

            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True

            return False

        return dfs(source)
        
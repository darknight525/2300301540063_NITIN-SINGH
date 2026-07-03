from collections import defaultdict
import heapq

class Solution:
    def findMaxPathScore(self, edges, online, k):

        n = len(online)

        graph = defaultdict(list)
        mx = 0
        mn = float("inf")

        for u, v, w in edges:
            graph[u].append((v, w))
            mx = max(mx, w)
            mn = min(mn, w)

        def check(limit):

            dist = [float("inf")] * n
            dist[0] = 0

            pq = [(0, 0)]

            while pq:

                cost, u = heapq.heappop(pq)

                if cost > dist[u]:
                    continue

                for v, w in graph[u]:

                    if w < limit:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    newCost = cost + w

                    if newCost < dist[v] and newCost <= k:
                        dist[v] = newCost
                        heapq.heappush(pq, (newCost, v))

            return dist[n - 1] <= k

        if mn == float("inf"):
            return -1

        lo, hi = mn, mx
        ans = -1

        while lo <= hi:

            mid = (lo + hi) // 2

            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
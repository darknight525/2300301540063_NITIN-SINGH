import heapq

class Solution(object):
    def kClosest(self, points, k):
        heap = []

        for x, y in points:
            dist = x * x + y * y

            heapq.heappush(heap, (-dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        ans = []

        for dist, x, y in heap:
            ans.append([x, y])

        return ans
        
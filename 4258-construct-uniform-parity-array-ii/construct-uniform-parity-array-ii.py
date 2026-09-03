class Solution(object):
    def uniformArray(self, nums1):
        mn = float('inf')

        for x in nums1:
            if x % 2 == 1:
                mn = min(mn, x)

        if mn == float('inf'):
            return True

        for x in nums1:
            if x % 2 == 0 and x < mn:
                return False

        return True
        
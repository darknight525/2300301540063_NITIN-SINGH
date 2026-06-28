class Solution(object):
    def numIdenticalPairs(self, nums):
        return sum(v*(v-1)//2 for v in Counter(nums).values())
        
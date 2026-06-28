class Solution(object):
    def findNumbers(self, nums):
        return sum(len(str(x))%2==0 for x in nums)
        
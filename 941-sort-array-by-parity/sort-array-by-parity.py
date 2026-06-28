class Solution(object):
    def sortArrayByParity(self, nums):
        return sorted(nums,key=lambda x:x%2)
        
class Solution(object):
    def subsets(self, nums):
       
    
        res = [[]]
        
        for num in nums:
            new_subsets = []
            for subset in res:
                new_subsets.append(subset + [num])
            res += new_subsets
        
        return res
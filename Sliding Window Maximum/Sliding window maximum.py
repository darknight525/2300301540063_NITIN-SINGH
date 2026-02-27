class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0:
            return []
        
        dq = deque()
        res = []
        
        for i in range(len(nums)):
            
           
            if dq and dq[0] == i - k:
                dq.popleft()
            
            
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)
            
            
            if i >= k - 1:
                res.append(nums[dq[0]])
        
        return res
        
    
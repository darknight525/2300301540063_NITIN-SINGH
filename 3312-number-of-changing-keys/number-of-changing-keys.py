class Solution(object):
    def countKeyChanges(self, s):
        s = s.lower()
        count = 0
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                count+=1
        
        return count
              
        
       
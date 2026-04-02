class Solution:
    def partition(self, s):
        res = []
        
        def dfs(path, remaining):
            if not remaining:
                res.append(path)
                return
            
            for i in range(len(remaining)):
                part = remaining[:i+1]
                
                if part == part[::-1]:
                    dfs(path + [part], remaining[i+1:])
        
        dfs([], s)
        return res
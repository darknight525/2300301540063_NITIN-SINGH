class Solution:
    def arrayRankTransform(self, arr):

        temp = sorted(set(arr))
        rank = {}
        currentRank = 1

        for num in temp:
            rank[num] = currentRank
            currentRank+=1
        
        ans = []

        for num in arr:
            ans.append(rank[num])

        
        return ans


        
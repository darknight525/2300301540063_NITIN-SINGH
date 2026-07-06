class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        while low < high :
            mid = ( low + high ) // 2
            hours = 0 

            for bananas in piles:
                hours+= (bananas + mid-1)//mid

            if hours <= h:
                high = mid
            else:
                low = mid+1
            
        
        return low

                
       
import math
from functools import lru_cache

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        
        # Using a top-down dynamic programming approach with a cache
        @lru_cache(None)
        def dp(i, gcd1, gcd2):
            # Base Case: processed all elements in the array
            if i == n:
                # Valid if both subsequences are non-empty (gcd > 0) 
                # and their greatest common divisors are equal.
                return 1 if gcd1 > 0 and gcd1 == gcd2 else 0
            
            # Choice 1: Do not include nums[i] in either subsequence
            ans = dp(i + 1, gcd1, gcd2)
            
            # Choice 2: Include nums[i] in the first subsequence
            new_gcd1 = nums[i] if gcd1 == 0 else math.gcd(gcd1, nums[i])
            ans = (ans + dp(i + 1, new_gcd1, gcd2)) % MOD
            
            # Choice 3: Include nums[i] in the second subsequence
            new_gcd2 = nums[i] if gcd2 == 0 else math.gcd(gcd2, nums[i])
            ans = (ans + dp(i + 1, gcd1, new_gcd2)) % MOD
            
            return ans

        # Start from index 0, with both initial GCD states set to 0 (meaning empty)
        return dp(0, 0, 0)

        
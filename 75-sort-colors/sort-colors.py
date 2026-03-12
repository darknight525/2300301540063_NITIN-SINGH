class Solution(object):
    def sortColors(self, nums):

        l = 0
        i = 0
        r = len(nums) - 1

        while i <= r:

            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1

            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1

            else:
                i += 1
        
           
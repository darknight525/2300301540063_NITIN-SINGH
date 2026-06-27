class Solution:
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        mp = {}

        for num in nums2:

            while stack and stack[-1] < num:
                mp[stack.pop()] = num

            stack.append(num)

        while stack:
            mp[stack.pop()] = -1

        return [mp[x] for x in nums1]
      
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        greater = {}
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                greater[smaller] = num 
            stack.append(num)

        for i in range(len(nums1)):
            nums1[i] = greater.get(nums1[i] , -1)
        
        return nums1
     
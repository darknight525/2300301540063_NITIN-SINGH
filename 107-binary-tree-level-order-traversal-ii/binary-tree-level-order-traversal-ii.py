# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []

        queue = deque([root])
        ans = []
        while queue:
            level = []
            size = len(queue)

            for i in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            ans.append(level)

        
        return ans[::-1]

        


       
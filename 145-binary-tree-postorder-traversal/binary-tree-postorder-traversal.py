# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans = []

    def postorder(self, root):
        # Base case
        if root is None:
            return
        
        # Left -> Right -> Root
        self.postorder(root.left)
        self.postorder(root.right)
        self.ans.append(root.val)

    def postorderTraversal(self, root):
        self.ans = []
        self.postorder(root)
        return self.ans
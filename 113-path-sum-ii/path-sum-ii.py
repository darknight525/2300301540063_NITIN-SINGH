# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):

        ans = []

        def dfs(root, targetSum, path):

            if not root:
                return

            path.append(root.val)

            if not root.left and not root.right:

                if root.val == targetSum:
                    ans.append(path[:])

            dfs(root.left, targetSum - root.val, path)
            dfs(root.right, targetSum - root.val, path)

            path.pop()

        dfs(root, targetSum, [])

        return ans
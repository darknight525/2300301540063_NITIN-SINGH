class Solution(object):
    def preorderTraversal(self, root):
        ans = []

        def dfs(node):
            if not node:
                return
            
            ans.append(node.val)

            dfs(node.left)
            
            dfs(node.right)

        dfs(root)
        return ans
class Solution:
    def goodNodes(self, root):

        def dfs(node, mx):

            if not node:
                return 0

            res = 1 if node.val >= mx else 0

            mx = max(mx, node.val)

            res += dfs(node.left, mx)
            res += dfs(node.right, mx)

            return res

        return dfs(root, root.val)
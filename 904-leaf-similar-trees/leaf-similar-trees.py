class Solution:
    def leafSimilar(self, root1, root2):

        def dfs(node, leaves):

            if not node:
                return

            if not node.left and not node.right:
                leaves.append(node.val)

            dfs(node.left, leaves)
            dfs(node.right, leaves)

        a = []
        b = []

        dfs(root1, a)
        dfs(root2, b)

        return a == b
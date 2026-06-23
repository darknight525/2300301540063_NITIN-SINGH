from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):

        if not root:
            return []

        q = deque([root])
        res = []
        leftToRight = True

        while q:

            level = []

            for _ in range(len(q)):

                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if not leftToRight:
                level.reverse()

            res.append(level)

            leftToRight = not leftToRight

        return res
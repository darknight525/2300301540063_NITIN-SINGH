from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):

        if not root:
            return []

        queue = deque([root])

        ans = []

        leftToRight = True

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

            if not leftToRight:
                level.reverse()

            ans.append(level)

            leftToRight = not leftToRight

        return ans
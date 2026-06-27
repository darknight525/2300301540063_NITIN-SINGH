from collections import deque

class Solution:
    def levelOrder(self, root):

        if not root:
            return []

        q = deque([root])
        ans = []

        while q:

            level = []

            for _ in range(len(q)):

                node = q.popleft()

                level.append(node.val)

                for child in node.children:
                    q.append(child)

            ans.append(level)

        return ans
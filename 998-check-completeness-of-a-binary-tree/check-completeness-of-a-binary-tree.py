from collections import deque

class Solution:
    def isCompleteTree(self, root):

        q = deque([root])

        null_seen = False

        while q:

            node = q.popleft()

            if node is None:
                null_seen = True
            else:

                if null_seen:
                    return False

                q.append(node.left)
                q.append(node.right)

        return True
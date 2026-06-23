class BSTIterator:

    def __init__(self, root):
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left

    def next(self):

        node = self.stack.pop()

        curr = node.right

        while curr:
            self.stack.append(curr)
            curr = curr.left

        return node.val

    def hasNext(self):
        return len(self.stack) > 0
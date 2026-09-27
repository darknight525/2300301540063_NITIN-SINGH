class Solution(object):
    def reverseParentheses(self, s):
        stack = []

        for ch in s:
            if ch == ')':
                temp = ""

                while stack[-1] != '(':
                    temp += stack.pop()

                stack.pop()  # remove '('

                for c in temp:
                    stack.append(c)
            else:
                stack.append(ch)

        return ''.join(stack)
        
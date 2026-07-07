class Solution(object):
    def sumAndMultiply(self, n):
        s = "".join(ch for ch in str(n) if ch != "0")

        if not s:
            return 0

        return int(s) * sum(int(ch) for ch in s)
      
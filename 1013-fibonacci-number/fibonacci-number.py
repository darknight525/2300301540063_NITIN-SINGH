class Solution(object):
    def fib(self, n):
        #Base Case 
        if n==0 or n==1:
            return n
        #Recursive Base
        return self.fib(n-1) + self.fib(n-2)
       
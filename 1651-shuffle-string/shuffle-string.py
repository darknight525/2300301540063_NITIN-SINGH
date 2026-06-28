class Solution(object):
    def restoreString(self, s, indices):
        return ''.join(x for _,x in sorted(zip(indices,s)))
       
        
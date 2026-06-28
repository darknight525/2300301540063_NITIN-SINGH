class Solution(object):
    def findComplement(self, num):
       return num^((1<<num.bit_length())-1)
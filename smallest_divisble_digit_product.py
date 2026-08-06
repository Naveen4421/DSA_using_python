class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            product = 1
            for ch in str(n):
                product *= int(ch)
            if product % t == 0:
                return n
            n += 1
        

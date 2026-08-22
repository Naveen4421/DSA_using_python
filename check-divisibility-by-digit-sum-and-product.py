class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digits = list(str(n))
        add = 0
        pro = 1
        for d in digits:
            add += int(d)
            pro *= int(d)
        total = add + pro
        if n % total == 0:
            return True
        else:
            return False

        

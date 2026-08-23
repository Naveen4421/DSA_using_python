class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        half_diff = 0.0
        for i in range(n // 2):
            half_diff += 4.5 if num[i] == '?' else int(num[i])
        for i in range(n // 2, n):
            half_diff -= 4.5 if num[i] == '?' else int(num[i])
        return half_diff != 0
            
        
        

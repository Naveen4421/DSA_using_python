class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dist = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        for i in range(len(s)):
            curr = dist[s[i]]
            if i + 1 < len(s) and curr < dist[s[i+1]]:
                total -= curr
            else:
                total += curr
        return total
        

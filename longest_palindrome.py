class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        s=Counter(s)
        total=0
        has_leftover = False

        for freq in s.values():
            if freq%2==0:
                total+=freq
            elif freq%2==1:
                total+=freq-1
                has_leftover = True
                
        if has_leftover:
            total += 1

        
        return total

        

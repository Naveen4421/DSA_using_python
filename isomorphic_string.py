class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        result1 = {}
        result2 = {}

        for i in range(len(s)):

            if s[i] in result1:
                if result1[s[i]] != t[i]:
                    return False

            if t[i] in result2:
                if result2[t[i]] != s[i]:
                    return False

            result1[s[i]] = t[i]
            result2[t[i]] = s[i]

        return True
                

            

        

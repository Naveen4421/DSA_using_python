def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen={}
        for i,c in enumerate(s):
            seen[c]=seen.get(c,0)+1
        for i,c in enumerate(s):
            if seen[c]==1:
                return i
        return -1

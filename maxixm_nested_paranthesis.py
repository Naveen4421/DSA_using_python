class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count=0
        count=0
        for i in range(len(s)):
            if s[i]=="(":
                count+=1
                max_count=max(max_count,count)

            elif s[i]==")":
                count-=1
        return max_count

        

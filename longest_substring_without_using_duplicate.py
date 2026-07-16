class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        array=set()
        left=0
        max_sub=0
        for i in range(len(s)):
            while s[i] in array:
                array.remove(s[left])
                left+=1
            array.add(s[i])
            max_sub=max(max_sub,i-left+1)
            
        return max_sub
        

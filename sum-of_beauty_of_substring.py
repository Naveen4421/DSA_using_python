class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        for i in range(len(s)):
            freq = {}

            for j in range(i, len(s)):
                
                freq[s[j]] = freq.get(s[j], 0) + 1

                
                max_freq = max(freq.values())
                min_freq = min(freq.values())

                
                ans += max_freq - min_freq

        return ans
        

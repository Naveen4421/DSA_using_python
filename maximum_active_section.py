class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = '1' + s + '1'
        
        # Split t into contiguous blocks of identical characters
        blocks = []
        i = 0
        n = len(t)
        
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            blocks.append((t[i], j - i))
            i = j
            
        initial_ones = s.count('1')
        max_delta = 0
        
        # Look for a '1' block surrounded by '0' blocks
        # Such a block must be at index k where 0 < k < len(blocks) - 1
        for k in range(1, len(blocks) - 1):
            char, length = blocks[k]
            if char == '1':
                # Check if both neighbors are '0' blocks
                if blocks[k - 1][0] == '0' and blocks[k + 1][0] == '0':
                    z_left = blocks[k - 1][1]
                    z_right = blocks[k + 1][1]
                    max_delta = max(max_delta, z_left + z_right)
                    
        return initial_ones + max_delta

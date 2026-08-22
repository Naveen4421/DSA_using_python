class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        from collections import Counter
        counter = Counter(s)
        result = []
        for char, count in counter.most_common():
            result.append(char * count)
        return ''.join(result)

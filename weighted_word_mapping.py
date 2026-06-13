class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        return ''.join(
            chr(ord('z') - (
                sum(weights[ord(c) - ord('a')] for c in word) % 26
            ))
            for word in words
        )

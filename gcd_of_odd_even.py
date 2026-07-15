class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        odd=0
        even=0
        count=1
        evencount=2
        for i in range(n):
            #count=1
            odd+=count
            count+=2
        for i in range(n):
            even+=evencount
            evencount+=2

        return even-odd
        

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        nums=Counter(nums)
        for ch,freq in nums.items():
            if freq!=1:
                return ch
        
        

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        n=len(nums)
        nums=Counter(nums)
        result=[]
        for ch,freq in nums.items():
            if freq>n/3:
                result.append(ch)
        return result        

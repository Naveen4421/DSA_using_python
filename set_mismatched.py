class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        n=len(nums)
        nums=Counter(nums)
        duplicate=0
        missing=0
        for num in range(1,n+1):
            if nums[num]==2:
                duplicate=num
            if nums[num]==0:
                missing=num
        
        return [duplicate ,missing]
        

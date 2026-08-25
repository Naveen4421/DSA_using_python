class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num=set(nums)
        multiple =k
        while multiple in num:
            multiple+=k
        return multiple

        

class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val=float('inf')
        max_val=float('-inf')
        min_index=0
        max_index=0
        for i in range(len(nums)):
            if nums[i]>max_val:
                max_val=nums[i]
                max_index=i
            if nums[i]<min_val:
                min_val=nums[i]
                min_index=i
        n=len(nums)
        lo = min(min_index, max_index)
        hi = max(min_index, max_index)

        
        from_front = hi + 1
        
        from_back = n - lo
        
        from_both = (lo + 1) + (n - hi)

        return min(from_front, from_back, from_both)
        


        

class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count={}
        left=0
        max_length=0
        for right in range(len(nums)):
            count[nums[right]]=count.get(nums[right],0)+1
            while count[nums[right]]>k:
                count[nums[left]]-=1
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length
        

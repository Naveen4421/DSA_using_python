def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr=maxi=nums[0]
        for i in range(1,len(nums)):
            curr=max(nums[i],curr+nums[i])
            maxi=max(maxi,curr)
        return maxi

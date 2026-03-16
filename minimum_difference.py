def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        if(k==1 or k==0):
            return 0
        nums.sort()
        n=len(nums)
        min_value = float('inf')
        for i in range(n-k+1):
            count=nums[i+k-1]-nums[i]
            min_value=min(count,min_value)
        return min_value

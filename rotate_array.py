def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k==0:
            return
        n=len(nums)
        k=k%n
        result=[]
        for i in range(n-k,n):
            result.append(nums[i])
        for j in range(n-k):
            result.append(nums[j])
        for i in range(n):
            nums[i]=result[i]

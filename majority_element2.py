def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for num in nums:
            c=0
            for i in nums:
                if num==i:
                    c+=1
                if c>n//2:
                    return num

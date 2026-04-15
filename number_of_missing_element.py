def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        nums=set(nums)
        result=[]
        for i in range(1,n+1):
            if i not in nums:
                result.append(i)
        return result

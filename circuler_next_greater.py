def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        result=[]
        for i in range(n):
            found=-1
            for j in range(1,n):
                if nums[(i+j)%n]>nums[i]:
                    found=nums[(i+j)%n]
                    break
            result.append(found)

        return result

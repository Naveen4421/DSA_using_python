class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        total=nums[0]
        for j in range(1,n):
            if nums[j]==nums[j-1]+1 :
                total+=nums[j]
            else:
                break
        num_set=set(nums)
        x=total
        while x in num_set:
            x+=1
        return x
        
        

class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        smallest=min(nums)
        largest=max(nums)
        value=[]
        result=[]
        for i in range(smallest+1,largest):
            value.append(i)
        for i in range(smallest+1,largest):
            if i not in nums:
                result.append(i)
        return result

        

class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)==k:
            return max(nums)
        count={}
        n=len(nums)
        for i in range(n-k+1):
            seen=set()
            for j in range(i,i+k):
                seen.add(nums[j])
            for x in seen:
                count[x]=count.get(x,0)+1
        ans=-1
        for j in count:
            if count[j]==1:
                ans=max(ans,j)
        return ans


        
        

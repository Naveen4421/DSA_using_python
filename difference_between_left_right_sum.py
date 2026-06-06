class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftsum=[0]
        rightsum=[0]
        ans=[]
        for i in range(len(nums)-1):
            val=leftsum[i]+nums[i]
            #print(leftsum[i])
            leftsum.append(val)
            #print(leftsum[i])
        #rint(leftsum,"\n")
        for i in range(len(nums)-1,0,-1):
            #print(nums[i])
            val=nums[i]+rightsum[0]
            rightsum.insert(0,val)
            #print(rightsum[0])
        #print(rightsum)
        for i in range(len(nums)):
            ind=leftsum[i]-rightsum[i]
            ans.append(abs(ind))
        return ans

        

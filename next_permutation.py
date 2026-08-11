
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        pivot=-1
        #find pivot element
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                pivot=i
                break
        # swap elements

        if pivot!=-1:
            for i in range(n-1,pivot,-1):
                if nums[i]>nums[pivot]:
                    nums[i],nums[pivot]=nums[pivot],nums[i]
                    break
        
        # reverse elemet swap

        left,right=pivot+1,n-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        return nums
